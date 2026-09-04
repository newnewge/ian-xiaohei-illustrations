#!/usr/bin/env python3
"""Tony 配图 · 中文手写标注叠字引擎
用法: python3 overlay.py <spec.json>
spec: {"base": "底图.png", "out": "输出.png", "labels": [
  {"text": "断点", "x": 0.5, "y": 0.1, "size": 44, "color": "black|red|orange",
   "rot": -4, "jitter": 2, "anchor": "la"}]}
x,y 为画布比例; jitter=逐字符随机位移像素(手写感); rot=整串旋转角
"""
import json, random, sys
from PIL import Image, ImageDraw, ImageFont

TTC = "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/13b8ce423f920875b28b551f9406bf1014e0a656.asset/AssetData/Xingkai.ttc"
COLORS = {"black": (26, 26, 26, 255), "red": (199, 57, 47, 255), "orange": (232, 115, 58, 255)}
SEED = 42  # 固定抖动,保证可复现


def load_font(size):
    # 探测 .ttc 里 STXingkaiSC-Light 的 face index
    for idx in range(6):
        try:
            f = ImageFont.truetype(TTC, size, index=idx)
            name = "-".join(f.getname())
            if "XingkaiSC" in name:
                return f
        except Exception:
            break
    return ImageFont.truetype(TTC, size)


def draw_label(base, spec, rng):
    W, H = base.size
    size = int(spec.get("size", 44) * W / 1360)  # 按宽度归一
    font = load_font(size)
    text, color = spec["text"], COLORS[spec.get("color", "black")]
    jit = int(spec.get("jitter", 2) * W / 1360)
    pad = size
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x, y = spec["x"] * W, spec["y"] * H
    anchor = spec.get("anchor", "la")  # la=左上 mm=居中 等
    if jit:
        # 逐字符微抖 → 手写感
        cx = x
        for ch in text:
            dy = rng.randint(-jit, jit)
            d.text((cx, y + dy), ch, font=font, fill=color)
            cx += d.textlength(ch, font=font) + rng.randint(-1, 2)
    else:
        d.text((x, y), text, font=font, fill=color, anchor=anchor)
    rot = spec.get("rot", 0)
    if rot:
        # 绕文字区域中心旋转
        bbox = layer.getbbox()
        if bbox:
            cx0, cy0 = (bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2
            layer = layer.rotate(rot, center=(cx0, cy0), resample=Image.BICUBIC)
    return Image.alpha_composite(base, layer)


def main():
    spec = json.load(open(sys.argv[1]))
    rng = random.Random(SEED)
    base = Image.open(spec["base"]).convert("RGBA")
    # 先盖白补丁(伪文字残迹), 再叠字
    for wo in spec.get("whiteouts", []):
        W, H = base.size
        x0, y0 = int(wo["x"] * W), int(wo["y"] * H)
        x1, y1 = int((wo["x"] + wo["w"]) * W), int((wo["y"] + wo["h"]) * H)
        patch = ImageDraw.Draw(base)
        patch.rectangle([x0, y0, x1, y1], fill=(255, 255, 255, 255))
    for lb in spec.get("labels", []):
        base = draw_label(base, lb, rng)
    base.convert("RGB").save(spec["out"], "PNG")
    print(f"[overlay] {spec['out']} <- {len(spec.get('whiteouts', []))}白补丁 + {len(spec.get('labels', []))}标注")


if __name__ == "__main__":
    main()
