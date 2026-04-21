# 📋 PHÂN TÍCH & KẾT LUẬN LAB TÌMM KIẾM BFS - DFS

## 🎯 Kết Quả Thực Nghiệm

### 1. BẢN ĐỒ CƠ BẢN (5x5)
```
BFS: 16 ô duyệt
DFS: 11 ô duyệt
```

### 2. BẢN ĐỒ KHÓ (10x10)
```
BFS (thứ tự gốc):  53 ô duyệt
BFS (thứ tự mới):  49 ô duyệt
DFS (thứ tự gốc):  24 ô duyệt
DFS (thứ tự mới):  60 ô duyệt
```

---

## 📊 So Sánh BFS vs DFS

### BFS (Breadth-First Search)
- **Cấu trúc dữ liệu:** Queue (deque)
- **Đặc điểm:** Tìm kiếm theo chiều rộng, khám phá từng tầng
- **Ưu điểm:**
  - Tìm đường đi ngắn nhất (nếu tất cả cạnh có trọng số bằng nhau)
  - Tìm thấy mục tiêu nhanh trong bài toán có mục tiêu nông
- **Nhược điểm:**
  - Tốn bộ nhớ nhiều (lưu tất cả nút ở một tầng)
  - Chậm trong bài toán có độ sâu lớn

### DFS (Depth-First Search)
- **Cấu trúc dữ liệu:** Stack (list)
- **Đặc điểm:** Tìm kiếm theo chiều sâu, đi xuống sâu trước
- **Ưu điểm:**
  - Tiết kiệm bộ nhớ (chỉ lưu đường dẫn hiện tại)
  - Nhanh trong bài toán có mục tiêu sâu
- **Nhược điểm:**
  - Có thể bị lạc hướng (đi sâu vào đường cụt)
  - **Phụ thuộc mạnh vào thứ tự các hướng di chuyển!**

---

## 🔍 Quan Sát Quan Trọng

### 1. **Thứ Tự Hướng Di Chuyển Ảnh Hưởng Thế Nào?**

#### BFS:
- Thứ tự gốc (Lên, Xuống, Trái, Phải): **53 ô**
- Thứ tự mới (Phải, Lên, Xuống, Trái):  **49 ô**
- ✅ **Thay đổi: -4 ô** (giảm 8%)
- Nhưng BFS vẫn có cùng chiến lược khám phá (chiều rộng)

#### DFS:
- Thứ tự gốc (Lên, Xuống, Trái, Phải): **24 ô**
- Thứ tự mới (Phải, Lên, Xuống, Trái):  **60 ô**
- ❌ **Thay đổi: +36 ô** (tăng 150%!)
- DFS rất nhạy cảm với thứ tự vì nó tham lam

### 2. **Tối Ưu Hóa Bộ Nhớ**

```
Bản đồ 10x10 (100 ô):
- BFS duyệt: 53 ô (53% bản đồ)
- DFS duyệt: 24 ô (24% bản đồ)  ✨ TIẾT KIỆM HƠN 55%!
```

---

## 💡 Kết Luận Chính

### ✅ **1. DFS Tối Ưu Hơn BFS Về Bộ Nhớ**
- **Lý do:** DFS chỉ giữ một đường dẫn trong stack, không lưu toàn bộ tầng
- **Ứng dụng thực:** Khi bộ nhớ hạn chế (robot, IoT), DFS tốt hơn

### ✅ **2. Thứ Tự Hướng Rất Quan Trọng Cho DFS**
- **Thay đổi thứ tự → kết quả hoàn toàn khác** (24 → 60 ô)
- **Lý do:** DFS tham lam, phụ thuộc vào hướng được thử trước tiên
- **Lợi ích:** Có thể tối ưu DFS bằng cách chọn hướng hợp lý (ví dụ: ưu tiên hướng đến goal)

### ✅ **3. BFS Ổn Định Hơn**
- **Thay đổi thứ tự ít ảnh hưởng** (53 → 49 ô, -8%)
- **Lý do:** BFS khám phá hệ thống, không bị ảnh hưởng nhiều bởi thứ tự hướng

### ✅ **4. Chọn Thuật Toán Nào?**

| Tình Huống | Thuật Toán | Lý Do |
|-----------|-----------|--------|
| Cần tìm đường đi **ngắn nhất** | **BFS** | Bảo đảm tìm thấy đường ngắn nhất |
| **Bộ nhớ hạn chế** | **DFS** | Duyệt ít ô, tiết kiệm stack |
| **Độ sâu mục tiêu nhỏ** | **BFS** | Tìm nhanh hơn |
| **Độ sâu mục tiêu lớn** | **DFS** | Tốn ít bộ nhớ |
| **Cần cải thiện hiệu năng** | **DFS + hướng hợp lý** | Có thể tìm thấy nhanh gấp 2-3 lần |

---

## 🚀 Đề Xuất Cải Thiện

### 1. **Sử Dụng Heuristic (A* Search)**
- Kết hợp DFS + hướng ưu tiên theo khoảng cách đến mục tiêu
- Có thể giảm ô duyệt xuống dưới 10 ô

### 2. **Bidirectional Search**
- Tìm kiếm từ cả Start và Goal cùng lúc
- Giảm không gian tìm kiếm

### 3. **Greedy Best-First Search**
- Ưu tiên hướng gần Goal nhất
- Tìm nhanh nhưng không bảo đảm đường ngắn nhất

---

## 📝 Tóm Tắt Cho Báo Cáo

**Bài Lab đã hoàn thành các mục tiêu:**
✅ Cài đặt BFS với Queue  
✅ Cài đặt DFS với Stack  
✅ Thay đổi thứ tự hướng → Thấy DFS ảnh hưởng lớn (24→60 ô)  
✅ Tạo bản đồ 10x10 khó → So sánh: DFS = 24 ô, BFS = 53 ô  
✅ Kết luận: **DFS tối ưu 55% bộ nhớ hơn BFS**

