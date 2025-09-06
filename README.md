# SHOOT 'EM UP - Game 2D Pygame

## Giới thiệu

**SHOOT 'EM UP** là một game luyện tập kỹ năng ngắm bắn 2D được phát triển bằng Pygame. Game mô phỏng cơ chế tương tự Aim Lab với việc bắn các đầu zombie xuất hiện ngẫu nhiên trên màn hình.

## Tính năng

- 🎯 Zombie spawn ngẫu nhiên mỗi 3 giây
- 🔫 Click để bắn và tiêu diệt zombie
- 📊 Hệ thống tính điểm Hit/Miss
- 🎵 Background music và sound effects
- 📈 Tracking độ chính xác  
- 🎮 Difficulty tăng dần theo thời gian
- 🎶 Audio controls (mute, pause/resume)

## Yêu cầu Hệ thống

- Python 3.8 trở lên
- Pygame 2.5.0 trở lên
- Windows/Mac/Linux

## Cài đặt

### 1. Clone repository
```bash
git clone <repository-url>
cd btl1
```

### 2. Tạo virtual environment (khuyên dùng)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 4. Chạy game
```bash
python main.py
```

## Cách chơi

1. **Khởi động game**: Chạy `python main.py`
2. **Mục tiêu**: Click vào các đầu zombie khi chúng xuất hiện
3. **Timing**: Mỗi zombie tồn tại trong 1.3 giây
4. **Điểm số**: 
   - Hit: +10 điểm
   - Miss: -2 điểm
5. **Accuracy**: Theo dõi tỷ lệ % hit/total shots
6. **Audio**: Background music tự động phát, sound effects khi bắn/hit

## Controls

- **Mouse**: Di chuyển crosshair
- **Left Click**: Bắn
- **ESC**: Thoát game/Back to menu
- **M**: Mute/Unmute background music
- **P**: Pause/Resume background music

## Cấu trúc Dự án

```
btl1/
├── main.py                 # Entry point
├── src/                    # Source code
│   ├── game.py            # Game manager
│   ├── zombie.py          # Zombie class
│   ├── player.py          # Player input
│   ├── ui.py              # User interface
│   └── settings.py        # Game settings
├── assets/                 # Game assets
│   ├── images/            # Sprites, backgrounds
│   └── sounds/            # Audio files
└── requirements.txt       # Dependencies
```

## License

Dự án này được phát triển cho mục đích học tập - Assignment 1 Môn Lập trình game HCMUT 251.

---

**Happy Shooting! 🎯**
