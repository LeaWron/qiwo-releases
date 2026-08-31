# 齐我输入法 · 下载

Qiwo Input Method —— 基于 [RIME | 中州韵输入法引擎](https://rime.im)、
默认搭载[白霜拼音](https://github.com/gaboolic/rime-frost)的跨平台输入法。
数据完全本地处理，支持自托管 WebDAV 跨设备同步词库与配置。

## 下载

所有版本见 [Releases 列表](https://github.com/LeaWron/qiwo-releases/releases)，按 tag 前缀区分端：

| 平台 | tag 前缀 | 说明 |
|------|----------|------|
| Windows 输入法 | `win-v*` | 安装包（x64 / Win32），可与小狼毫共存安装；内置检查更新 |
| 桌面助手 | `companion-v*` | WebDAV 同步/设置工具（Windows/macOS/Linux），从输入法托盘菜单「齐我助手」打开 |
| macOS 输入法 | `mac-v*`（即将发布） | Qiwo.app 压缩包附 `install.sh`，macOS 13+，通用二进制 |
| Android | 即将发布 | 单 APK，装完即用（内置白霜） |
| Linux | 规划中 | ibus 引擎，源码构建脚本已就绪 |

> Windows 提示「未知发布者」、macOS 提示无法验证开发者均属预期（未做代码签名，
> macOS 首次运行按 `install.sh` 提示放行）；
> 与原版小狼毫共存安装没问题，但两者共享 Rime 用户目录，**不建议同时运行**。

## 更新源

- Windows 稳定通道：`appcast/win.xml`（安装后「检查新版本」自动使用，发版时 CI 自动改写）
- Windows 测试通道：`appcast/win-testing.xml`（注册表 `HKCU\Software\Qiwo` 下
  `UpdateChannel` 设为 `testing` 启用）
- macOS：`appcast/mac.xml`（应用内 Sparkle 自动检查，更新包经 Ed25519 签名）

## 致谢

Qiwo 构建于以下开源项目之上：[librime](https://github.com/rime/librime)、
[weasel](https://github.com/rime/weasel)、[fcitx5-android](https://github.com/fcitx5-android/fcitx5-android)、
[rime-frost](https://github.com/gaboolic/rime-frost) 等。各端源码依相应
开源许可证（GPLv3 / LGPL-2.1 等）提供。
