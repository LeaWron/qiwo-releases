# 齐我输入法 · 下载

Qiwo Input Method —— 基于 [RIME | 中州韵输入法引擎](https://rime.im)、
默认搭载[白霜拼音](https://github.com/gaboolic/rime-frost)的跨平台输入法。
数据完全本地处理，支持自托管 WebDAV 跨设备同步词库与配置。

## 下载

所有版本见 [Releases 列表](https://github.com/LeaWron/qiwo-releases/releases)，按 tag 前缀区分端。
各端版本号独立递增，互不相干。

| 平台 | tag 前缀 | 当前 | 说明 |
|------|----------|------|------|
| Windows | `win-v*` | 0.2.7 | 单个安装器，内含 x64 与 32 位组件；ARM64 的 Win11 装 x64 那份。可与小狼毫共存 |
| macOS | `mac-v*` | 0.1.0 | 压缩包附 `install.sh`；macOS 13.0+，通用二进制（Intel / Apple Silicon） |
| Linux | `lin-v*` | 0.1.1 | IBus 引擎；压缩包附 `install.sh`，装到 `/usr` |
| Android | `android-v*` | 0.2.2 | 单 APK，装完即用（内置白霜）；Android 6.0+，四个 ABI 各一个包 |
| 桌面助手 | `companion-v*` | 0.1.4 | **不用单独下载**，见下 |

### 桌面助手随输入法一起装

`companion-v*` 这个通道是给构建流程用的：Windows / macOS / Linux 的输入法安装包
都已经把助手打包在里面，装完输入法就有，从输入法托盘菜单的「齐我助手」打开。

单独下 `companion-v*` 里的文件没有用——那是给各端打包时取用的裸产物，
放到哪里、怎么被输入法找到，都由安装包决定。

### 安装

- **Windows**：运行 `qiwo-*-installer.exe`
- **macOS**：解包后 `./install.sh`（不提供 dmg：没有代码签名，dmg 装法容易被系统拦下）
- **Linux**：解包后 `./install.sh`，然后在 IBus 设置里添加「齐我输入法」
- **Android**：按机器架构选 APK（不确定就选 `arm64-v8a`）

> Windows 提示「未知发布者」、macOS 提示无法验证开发者均属预期（未做代码签名，
> macOS 首次运行按 `install.sh` 提示放行）；
> 与原版小狼毫共存安装没问题，但两者共享 Rime 用户目录，**不建议同时运行**。

Android 的 APK 全部由同一个证书签名（SHA-256
`1c1b542012c0a362445ec828e7acb76bcbe238cc39bc5b30bf920f98c0ab0780`），
换版本可以直接覆盖安装。发布流程会逐个校验这个指纹，签错 key 的包发不出来。

## 更新

四个端都能在应用内检查并完成更新，不需要手动来这里下载：

| 平台 | 入口 | 机制 |
|------|------|------|
| Windows | 托盘菜单「检查更新」 | WinSparkle，读 `appcast/win.xml` |
| macOS | 输入法菜单「检查更新」 | Sparkle，读 `appcast/mac.xml`，更新包经 Ed25519 签名 |
| Linux | IBus 面板「检查更新」 | 拉起齐我助手 → 下载安装包 → `pkexec` 提权安装 → 重启 ibus |
| Android | 设置 → Qiwo → 检查更新 | 直接查 GitHub Releases API 的 `android-v*`，下载 APK 后调起系统安装器；打开设置界面时也会自动检查，每天最多一次 |

齐我助手里的「检查更新」会同时报告助手和本机输入法的版本；由于助手随输入法分发，
可执行的更新动作永远落在输入法上。

Windows 另有测试通道 `appcast/win-testing.xml`，在注册表
`HKCU\Software\Qiwo` 下把 `UpdateChannel` 设为 `testing` 启用。

## 致谢

Qiwo 构建于以下开源项目之上：[librime](https://github.com/rime/librime)、
[weasel](https://github.com/rime/weasel)、[squirrel](https://github.com/rime/squirrel)、
[ibus-rime](https://github.com/rime/ibus-rime)、
[fcitx5-android](https://github.com/fcitx5-android/fcitx5-android)、
[rime-frost](https://github.com/gaboolic/rime-frost) 等。各端源码依相应
开源许可证（GPLv3 / LGPL-2.1 等）提供。
