# 齐我输入法 · 下载

Qiwo Input Method —— 基于 [RIME | 中州韵输入法引擎](https://rime.im)、
默认搭载[白霜拼音](https://github.com/gaboolic/rime-frost)的跨平台输入法。
数据完全本地处理，支持自托管 WebDAV 跨设备同步词库与配置。

## 下载

| 平台 | 最新版 | 说明 |
|------|--------|------|
| Windows | [win-v0.1.0](https://github.com/LeaWron/qiwo-releases/releases/tag/win-v0.1.0) | 安装包（x64 / Win32），可与小狼毫共存安装 |
| Android | 即将发布 | 单 APK，装完即用（内置白霜） |
| Linux / macOS | 规划中 | — |

> Windows 提示「未知发布者」属预期（未做代码签名）；
> 与原版小狼毫共存安装没问题，但两者共享 Rime 用户目录，**不建议同时运行**。

## 更新源

- Windows 稳定通道：`appcast/win.xml`（安装后「检查新版本」自动使用）
- Windows 测试通道：`appcast/win-testing.xml`（注册表 `HKCU\Software\Qiwo` 下
  `UpdateChannel` 设为 `testing` 启用）

## 致谢

Qiwo 构建于以下开源项目之上：[librime](https://github.com/rime/librime)、
[weasel](https://github.com/rime/weasel)、[fcitx5-android](https://github.com/fcitx5-android/fcitx5-android)、
[rime-frost](https://github.com/gaboolic/rime-frost) 等。各端源码依相应
开源许可证（GPLv3 / LGPL-2.1 等）提供。
