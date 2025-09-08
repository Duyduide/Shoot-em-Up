# SHOOT 'EM UP Game - Yêu cầu BTL và Tính năng bổ sung

## **Yêu cầu BTL**

### 1. **Hệ thống vẽ**
- **Sử dụng hàm `draw()` để vẽ**
  - Mỗi đối tượng game có method `draw()` riêng
  - `zombie.draw(screen)` - Vẽ zombie với animation
  - `ui.draw_menu()` - Vẽ giao diện menu
  - `ui.draw_game_ui()` - Vẽ HUD trong game
  - `ui.draw_game_over()` - Vẽ màn game over

### 2. **Animation hệ thống Zombie**
- **Đầu zombie có animation**
  - **Idle Animation**: 5 frames breathing effect (zombie-head-idle-1.png đến zombie-head-idle-5.png)
  - **Hit Animation**: 4 frames death effect (zombie-head-hit-1.png đến zombie-head-hit-4.png)
  - **Frame-based Animation System**: Sử dụng timer để chuyển đổi frames
  - **Sprite Loading**: Class-level caching để tối ưu hiệu suất

### 3. **Thời gian xuất hiện Zombie**
- **Đầu zombie xuất hiện trong khoảng 0.8s và biến mất**
  - `ZOMBIE_LIFETIME = 0.8` seconds 
  - Zombie tự động biến mất sau thời gian lifetime
  - Animation hit khi bị bắn trước khi biến mất

### 4. **Hệ thống bắn**
- **Sự kiện click chuột, xác định bắn trúng zombie**
  - `pygame.MOUSEBUTTONDOWN` event handling
  - Kiểm tra zombie bị bắn (click trúng) với `zombie.rect.collidepoint(pos)`
  - `zombie_manager.check_hit(pos)` để kiểm tra bắn trúng
  - Custom crosshair thay thế con trỏ chuột

### 5. **Hệ thống điểm số (Scoring System)**
- **Điểm số: hit/miss/accuracy**
  - **Hit Points**: +10 điểm khi bắn trúng zombie
  - **Miss Penalty**: -2 điểm khi bắn trượt
  - **Accuracy Calculation**: `(hits/total_shots) * 100%`
  - **Real-time Display**: Hiển thị score, accuracy, zombie count trong game

### 6. **Hệ thống âm thanh (Audio System)**
- **Có nhạc nền và âm thanh khi hit zombie**
  - **Background Music**: Theme music loop liên tục
  - **Sound Effects**:
    - Gun shot sound khi click chuột
    - Hit sound khi bắn trúng zombie
  - **Volume Control**: Điều chỉnh âm lượng music và SFX riêng biệt
  - **Audio Controls**: M (mute/unmute), P (pause/resume)

---

## **Tính năng bổ sung (Additional Features)**

### **Game States Management**
- Menu State với buttons Play/Quit
- Playing State với gameplay chính
- Game Over State với statistics

### **Multi-Spawn System**
- Nhiều zombies xuất hiện thành 1 cụm gần nhau (Cluster spawning)
- Spawn rate tăng dần theo thời gian

### **Visual Assets**
- Các assets đều được tự vẽ trên Piskel
- Background image từ assets
- Custom crosshair
- Zombie sprite animations