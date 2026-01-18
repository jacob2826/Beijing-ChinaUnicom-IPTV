# Beijing Unicom IPTV (Private)

该项目从指定的 m3u 源获取组播地址，转换为内网单播地址并输出到 Cloudflare Pages。

## 功能
- 拉取单个 m3u 源
- 将组播地址转换为单播地址
- 生成整理后的 m3u
- 由 GitHub Actions 每天自动更新并发布到 Cloudflare Pages

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
- 生成后的 m3u 输出到 `dist/` 目录
- 由 Cloudflare Pages 自动发布 `dist/`

## Cloudflare Pages 配置（必填）
GitHub Actions 发布需要以下 Secrets/Variables，否则会出现 `Input required and not supplied: apiToken` 报错：

- `CF_PAGES_TOKEN`：Cloudflare API Token，至少需要 Pages 的发布权限
- `CF_ACCOUNT_ID`（Variables）：Cloudflare 账户 ID
- `CF_PROJECT_NAME`（Variables）：Cloudflare Pages 项目名称（**Pages 控制台里显示的项目名**，不是自定义域名）

可在 GitHub 仓库 **Settings → Secrets and variables → Actions** 中新增以上 Secrets/Variables。

### CF_PROJECT_NAME 如何填写
`CF_PROJECT_NAME` 必须与 Cloudflare Pages 中已有的项目名完全一致（区分大小写）。可在 Cloudflare 控制台 **Pages → 选择项目 → 设置** 中查看项目名。它通常是你创建 Pages 项目时填写的名称，**不是** `xxx.pages.dev` 或自定义域名。
