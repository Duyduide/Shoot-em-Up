# SHOOT 'EM UP - Kế hoạch Dự án Game 2D

## Tổng quan Dự án

### Tên Game: SHOOT 'EM UP
### Thể loại: Action/Arcade - Aim Training Game
### Engine: Pygame (Python)
### Mục tiêu: Tạo game luyện tập aim tương tự Aim Lab với cơ chế bắn zombie

---

## Mô tả Game

Game "SHOOT 'EM UP" là một trò chơi luyện tập kỹ năng ngắm bắn, trong đó:
- Game có main menu với 2 nút: Play và Quit
- Mỗi lượt chơi kéo dài 30 giây
- Mỗi zombie tồn tại trong 1.3 giây trước khi biến mất
- Spawn rate tăng dần theo thời gian trong suốt 30 giây
- Người chơi cần click vào zombie để tiêu diệt
- Hệ thống tính điểm dựa trên độ chính xác (Hit/Miss)
---

## Tính năng Chính

### 1. Main Menu
- [x] **Play Button**: Bắt đầu game
- [x] **Quit Button**: Thoát khỏi game

### 2. Gameplay Core  
- [x] **30 Second Timer**: Mỗi lượt chơi kéo dài đúng 30 giây
- [x] **Zombie Lifetime**: Mỗi zombie tồn tại 1.3 giây
- [x] **Dynamic Spawn Rate**: Spawn rate tăng dần theo thời gian
- [x] **Click Detection**: Phát hiện click chuột trúng zombie
- [x] **Score System**: Tính điểm Hit/Miss và hiển thị thống kê

### 3. Visual & Audio
- [x] **Zombie Sprites**: Hình ảnh đầu zombie
- [x] **Background**: Nền game phù hợp  
- [x] **UI Elements**: Hiển thị score, timer
- [x] **Sound Effects**: Âm thanh bắn, hit, miss

---

## Cấu trúc Dự án

```
btl1/
├── main.py                 # File chính khởi chạy game
├── src/
│   ├── __init__.py
│   ├── game.py            # Class chính quản lý game
│   ├── zombie.py          # Class Zombie
│   ├── player.py          # Class Player (quản lý input)
│   ├── ui.py              # Class UI (score, menu)
│   ├── sound_manager.py   # Quản lý âm thanh
│   └── settings.py        # Các constants và settings
├── assets/
│   ├── images/
│   │   ├── zombie_head.png
│   │   ├── crosshair.png
│   │   └── background.png
│   └── sounds/
│       ├── shoot.wav
│       ├── hit.wav
│       └── miss.wav
├── requirements.txt       # Dependencies
└── README.md             # Hướng dẫn cài đặt và chạy
```

---

## Roadmap Phát triển

### Phase 1: Core Setup
- [ ] Cài đặt pygame và setup môi trường
- [ ] Tạo cửa sổ game cơ bản
- [ ] Implement game loop chính
- [ ] Setup input handling (mouse click)

### Phase 2: Basic Gameplay
- [ ] Tạo class Zombie
- [ ] Implement timer system (1.3 giây cho mỗi zombie, 30s total)
- [ ] Dynamic spawn rate system
- [ ] Collision detection cho mouse click
- [ ] Basic scoring system (Hit/Miss)

### Phase 3: Visual & Audio
- [ ] Thêm sprite cho zombie
- [ ] Tạo main menu với Play/Quit buttons
- [ ] Tạo background và UI elements
- [ ] Implement sound effects
- [ ] Visual feedback khi hit/miss

### Phase 4: Game Polish
- [ ] Game over screen sau 30 giây
- [ ] Statistics display (score, accuracy)
- [ ] Performance optimization

---

## Specifications Chi tiết

### Zombie Mechanics
```python
# Zombie Properties
- Types: Small và Large zombies
- Spawn Position: Random (x, y) trong screen bounds  
- Lifetime: 1.3 seconds
- Spawn Rate: Tăng dần trong suốt 30 giây
```

### Game Settings
```python
# Game Configuration
- Game Duration: 30 seconds per round
- Single Difficulty Level
- Main Menu: Play/Quit buttons only
```

### Scoring System
```python
# Score Calculation
- Hit: +10 points
- Miss: -5 points
- Accuracy: (Hits / Total_Shots) * 100%
```

---

## Assets Cần thiết

### Graphics
- [ ] Zombie head sprite (64x64, PNG với alpha)
- [ ] Crosshair cursor (32x32)
- [ ] Background texture hoặc gradient
- [ ] UI elements (buttons, score display)
- [ ] Particle effects cho hit/miss

### Audio
- [ ] Yêu cầu sử dụng file .wav
- [ ] Gunshot sound effect
- [ ] Hit confirmation sound
- [ ] Background music