# Beijing Unicom IPTV (Private)

该项目从指定的 m3u 源获取组播地址，转换为内网单播地址并输出到 GitHub 仓库，使用 rawcontent 地址直接访问。

## 功能
- 拉取单个 m3u 源
- 将组播地址转换为单播地址
- 生成整理后的 m3u
- 由 GitHub Actions 每天自动更新并提交到仓库

## 输入源
- https://raw.githubusercontent.com/qwerttvv/Beijing-IPTV/master/IPTV-Unicom-Multicast.m3u

## 单播地址示例
- 原始：rtp://239.3.1.129:8008
- 转换后：http://192.168.100.1:9999/rtp/239.3.1.129:8008

## 使用方式（本地）
```bash
python3 scripts/build_m3u.py > output.m3u
```

## GitHub Actions
- 每天自动运行一次
- 生成后的 m3u 输出到 `dist/` 目录并提交到仓库
- 使用 GitHub rawcontent 访问生成文件，例如：
  - `https://raw.githubusercontent.com/<OWNER>/<REPO>/<BRANCH>/dist/iptv.m3u`
