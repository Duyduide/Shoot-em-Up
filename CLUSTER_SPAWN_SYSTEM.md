# CLUSTER SPAWN SYSTEM

## Hệ thống Spawn Nhóm ✅

### 🎯 **Concept**
Thay vì zombies xuất hiện rải rác khắp màn hình, chúng giờ sẽ spawn thành **nhóm gần nhau** nhưng **không overlap**, tạo cảm giác tự nhiên và thử thách tập trung hơn.

### 📊 **Cluster Parameters**
```python
CLUSTER_RADIUS = 120           # Bán kính vùng cluster
MIN_CLUSTER_DISTANCE = 60      # Khoảng cách tối thiểu giữa zombies
CLUSTER_CENTER_VARIATION = 30  # Độ lệch từ tâm cluster
```

## Cơ chế Hoạt động

### 🎲 **1. Cluster Center Selection**
- Thuật toán tìm vị trí tốt nhất cho tâm cluster
- Tránh xa các zombie đang tồn tại
- Đảm bảo đủ không gian cho cả cluster
- Fallback về center màn hình nếu không tìm được vị trí tốt

### 👥 **2. Zombie Positioning**
- **Zombie đầu tiên**: Spawn rất gần tâm cluster (0-30px)
- **Zombies còn lại**: Spawn xung quanh trong bán kính 40-120px
- **Minimum distance**: 60px giữa các zombies trong cùng cluster
- **Random angles**: Tạo hình dạng cluster tự nhiên

### 🛡️ **3. Collision Avoidance**
- Kiểm tra khoảng cách với zombies khác trong cluster
- Kiểm tra khoảng cách với zombies đã có trên màn hình
- Đảm bảo không spawn ngoài boundaries màn hình
- Fallback position nếu không tìm được vị trí hợp lệ

## Visual Layout Examples

### Early Game (1 zombie)
```
     🧟
```

### Mid Game (2 zombies)
```
   🧟
     🧟
```

### Late Game (3 zombies)
```
  🧟   🧟
     🧟
```

## Technical Benefits

### ✅ **Gameplay Improvements**
- **Focused Challenge**: Player cần tập trung vào một khu vực
- **Natural Feel**: Zombies xuất hiện như một nhóm thực tế
- **Strategic Depth**: Player phải ưu tiên target nào trước
- **Visual Clarity**: Dễ nhận biết và theo dõi

### ✅ **Technical Advantages**
- **Smart Positioning**: Tránh overlap và edge cases
- **Performance**: Efficient cluster generation
- **Configurable**: Dễ dàng điều chỉnh parameters
- **Robust**: Fallback mechanisms cho edge cases

### ✅ **User Experience**
- **Less Eye Strain**: Không cần quét toàn màn hình
- **More Engaging**: Tạo cảm giác "nhiệm vụ tập trung"
- **Better Flow**: Gameplay rhythm tự nhiên hơn
- **Satisfying**: Feeling của clear một cluster

## Settings Tuning

### 🔧 **Cluster Size**
```python
CLUSTER_RADIUS = 120  # Smaller = tighter clusters
                      # Larger = more spread out
```

### 🔧 **Zombie Distance** 
```python
MIN_CLUSTER_DISTANCE = 60  # Smaller = zombies closer together
                           # Larger = more separated
```

### 🔧 **Center Variation**
```python
CLUSTER_CENTER_VARIATION = 30  # How much first zombie varies from center
```

## Game Balance Impact

### **Before**: Random scatter spawn
- Zombies anywhere on screen
- Hard to track multiple targets
- Less strategic gameplay

### **After**: Cluster spawn
- Zombies grouped together
- Focused engagement areas
- More tactical gameplay
- Better visual flow

---

## Implementation Files
- `src/zombie.py` - Core cluster spawn logic
- `src/settings.py` - Configurable parameters
- Enhanced `_generate_spawn_positions()` method
- New `_find_cluster_center()` method

**Status**: ✅ Implemented and optimized
