# 齐我输入法 · 下载

Qiwo Input Method —— 基于 [RIME | 中州韵输入法引擎](https://rime.im)、
默认搭载[白霜拼音](https://github.com/gaboolic/rime-frost)的跨平台输入法。
数据完全本地处理，支持自托管 WebDAV 跨设备同步词库与配置。

## 下载

所有版本见 [Releases 列表](https://github.com/LeaWron/qiwo-releases/releases)，按 tag 前缀区分端。
各端版本号独立递增，互不相干。

| 平台 | tag 前缀 | 当前 | 说明 |
|------|----------|------|------|
| Windows | `win-v*` | 0.2.17 | 单个安装器，内含 x64 与 32 位组件；ARM64 的 Win11 装 x64 那份。可与小狼毫共存 |
| macOS | `mac-v*` | 0.1.4 | 压缩包附 `install.sh`；macOS 13.0+，通用二进制（Intel / Apple Silicon） |
| Linux / IBus | `lin-v*` | 0.1.6 | IBus 引擎；压缩包附 `install.sh`，装到 `/usr` |
| Linux / Fcitx5 | `fcitx5-v*` | [0.1.7](https://github.com/LeaWron/qiwo-releases/releases/tag/fcitx5-v0.1.7) | Ubuntu 26.04 amd64 / X11；独立 deb，内置助手；Qt 私有 ABI 6.10.2 |
| Android | `android-v*` | 0.2.7 | 单 APK，装完即用（内置白霜）；Android 6.0+，四个 ABI 各一个包 |
| 桌面助手 | `companion-v*` | [0.1.14](https://github.com/LeaWron/qiwo-releases/releases/tag/companion-v0.1.14) | **不用单独下载**，见下 |

### 桌面助手随输入法一起装

`companion-v*` 这个通道是给构建流程用的：Windows / macOS / Linux 的输入法安装包
都已经把助手打包在里面，装完输入法就有，从输入法托盘菜单的「齐我助手」打开。

单独下 `companion-v*` 里的文件没有用——那是给各端打包时取用的裸产物，
放到哪里、怎么被输入法找到，都由安装包决定。

### 安装

- **Windows**：运行 `qiwo-*-installer.exe`
- **macOS**：解包后 `./install.sh`（不提供 dmg：没有代码签名，dmg 装法容易被系统拦下）
- **Linux / IBus**：解包后 `./install.sh`，然后在 IBus 设置里添加「齐我输入法」
- **Linux / Fcitx5**：安装对应 deb 后，以普通用户运行 `qiwo-fcitx5-setup enable`；已有其他 Fcitx5 配置时先阅读安装说明
- **Android**：按机器架构选 APK（不确定就选 `arm64-v8a`）

> Windows 提示「未知发布者」、macOS 提示无法验证开发者均属预期（未做代码签名，
> macOS 首次运行按 `install.sh` 提示放行）；
> 与原版小狼毫共存安装没问题，但两者共享 Rime 用户目录，**不建议同时运行**。

Android 的 APK 全部由同一个证书签名（SHA-256
`1c1b542012c0a362445ec828e7acb76bcbe238cc39bc5b30bf920f98c0ab0780`），
换版本可以直接覆盖安装。发布流程会逐个校验这个指纹，签错 key 的包发不出来。

## 更新

已发布的 Windows、macOS、IBus 和 Android 通道支持应用内更新：

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

## Fcitx5 发布通道

当前版本为 **[0.1.7](https://github.com/LeaWron/qiwo-releases/releases/tag/fcitx5-v0.1.7)**，使用独立的 `fcitx5-v*` 标签。下载 [amd64 deb](https://github.com/LeaWron/qiwo-releases/releases/download/fcitx5-v0.1.7/qiwo-fcitx5_0.1.7_amd64.deb) 和 [SHA-256 校验和](https://github.com/LeaWron/qiwo-releases/releases/download/fcitx5-v0.1.7/release-SHA256SUMS.txt)，在下载目录执行：

```sh
sha256sum -c release-SHA256SUMS.txt
sudo apt-get --no-remove --no-install-recommends install ./qiwo-fcitx5_0.1.5_amd64.deb
qiwo-fcitx5-setup enable
```

启用命令以桌面用户运行，保存工作后重新登录 X11。0.1.1 已通过旧版升级、设备 ID 与词库保留、重启后的自动启动，以及 Qt6 / GTK3 系统输入验收。当前只支持 Ubuntu 26.04 amd64 / X11，Wayland 和其他发行版尚未验收。

源码与构建说明位于 [qiwo-fcitx5](https://github.com/LeaWron/qiwo-fcitx5)（当前为私有源码仓库）。

0.1.2 起支持应用内更新：打开“齐我输入法设置”自动检查版本，或从托盘“检查更新”进入，有新版本时点击“立即更新”并完成系统授权。下载先校验，安装前备份词库，完成后恢复输入法并重新打开助手。0.1.1 首次升级需要手动安装最新版。不要安装 `lin-v*` 的 IBus 更新包。升级前结束输入和同步、关闭助手并退出 Fcitx5；安装新包后运行 `qiwo-fcitx5-setup enable`。回退使用 `qiwo-fcitx5-setup rollback`，用户词库与设备 ID 保留。

0.1.3 起支持定时自动同步：在设置中填写自动同步间隔并保存，0 关闭，1–10080 分钟开启。由 Fcitx5 本体执行，关闭助手仍有效；输入、部署或更新期间延后，失败后按间隔重试。旧配置默认关闭。

桌面助手统一使用 `companion-v*` 发布基线：三端构建与附件校验齐全后才公开，各输入法固定版本及源码提交取用，禁止某端先分发尚未正式发布的助手版本。输入法整包版本与助手版本分别显示。

Fcitx5 0.1.7 内置已正式通用发布的齐我助手 0.1.14，直接取用公开的同一 Linux 二进制；检查更新同时报告助手与输入法版本。助手随 Fcitx5 整包升级。

助手 0.1.12 的同步内容管理四端统一：Windows 0.2.15、macOS 0.1.2、IBus 0.1.4、Fcitx5 0.1.5 均接入本体执行。请同时升级助手和输入法本体，再使用清理；旧本体会显示升级提示。

助手 0.1.13 更新清理说明：先备份到本机，再删除所选残留。备份不参与 WebDAV 同步，也不会自动删除；旧设备再次同步时，文件可能重新出现。Windows 0.2.16、macOS 0.1.3、IBus 0.1.5、Fcitx5 0.1.6 统一内置该版本。

Android 0.2.7 支持自定义自动同步间隔：在 WebDAV 同步设置中填写分钟数，最小 15 分钟，默认 360 分钟。自动同步开关独立控制启用状态；修改间隔后更新已有后台任务。系统省电策略可能延迟实际执行。旧配置继续使用原有 6 小时周期。


助手 0.1.14 与 Windows 0.2.17、macOS 0.1.4、IBus 0.1.6、Fcitx5 0.1.7 接入安全同步：至少 5 秒无输入且无组词/候选状态后导出，网络期间允许输入；只合并实际变化的其他设备学习快照，等待真实完成后确认。同步结束不再无条件完整部署。配置、方案与基础词典的实际本机变更保留为待部署，重启、后续无变化同步、失败和取消都不会误清除；通过查看变更文件、重试合并和立即部署处理。设备备份缓存和未知用途文件保留检查记录。手动部署只清除开始时捕获的变更。
