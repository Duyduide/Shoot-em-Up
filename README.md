# SHOOT 'EM UP - Game 2D Pygame

## Giới thiệu

**SHOOT 'EM UP** là một game luyện tập kỹ năng ngắm bắn 2D được phát triển bằng Pygame. Game mô phỏng cơ chế tương tự Aim Lab với việc bắn các đầu zombie xuất hiện ngẫu nhiên trên màn hình.

## Tính năng

- 🎯 Zombie spawn ngẫu nhiên mỗi 3 giây
- 🔫 Click để bắn và tiêu diệt zombie
- 📊 Hệ thống tính điểm Hit/Miss
- 🎵 Sound effects và visual feedback
- 📈 Tracking độ chính xác
- 🎮 Difficulty tăng dần theo thời gian

## Yêu cầu Hệ thống

- Python 3.8 trở lên
- Pygame 2.5.0 trở lên
- Windows/Mac/Linux
- RAM: 512MB minimum
- Dung lượng: 100MB

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
3. **Timing**: Mỗi zombie tồn tại trong 3 giây
4. **Điểm số**: 
   - Hit: +10 điểm
   - Miss: -2 điểm
5. **Accuracy**: Theo dõi tỷ lệ % hit/total shots

## Controls

- **Mouse**: Di chuyển crosshair
- **Left Click**: Bắn
- **ESC**: Thoát game/Pause
- **R**: Restart game

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

## Development Status

- [x] Project planning
- [ ] Core gameplay implementation
- [ ] Visual assets integration
- [ ] Audio system
- [ ] UI/UX polish
- [ ] Testing & optimization

## Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## Roadmap

- **Phase 1**: Core mechanics (Zombie spawn, click detection)
- **Phase 2**: Scoring system và UI
- **Phase 3**: Visual/Audio enhancements
- **Phase 4**: Game polish và optimization
- **Phase 5**: Advanced features (power-ups, levels)

## License

Dự án này được phát triển cho mục đích học tập - Assignment BTL1.

## Contact

Nếu có vấn đề hoặc góp ý, vui lòng tạo issue trong repository.

---

**Happy Shooting! 🎯**
