# Nama : Agung Mubarok
# NIM  : 0110120196 
# Kelas: Sistem Informasi - 05

class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next
  
class LinkedList:
  def __init__(self, head = None):
    self.head = head
  
  def add_last(self, new_data):
    if self.head is None:
      self.head = Node(new_data)
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = Node(new_data)
  
  def cetak(self):
    if self.head is None:
      print('List kosong')
    else:
      current = self.head
      while current is not None:
        print(current.data, end=' ')
        current = current.next
      print()

  def sum_odd(self):
    # Menginisialisasi variabel current_node sama dengan node pertama di dalam list yaitu head
    current_node = self.head
    # Jika kosong
    if current_node is None:
      # Maka akan mengembalikan nilai 0
      return 0
    # Jika tidak kosong
    else:
      # Menginisialisasi variabel count sama dengan data dari node pertama
      count = current_node.data
      # Variabel result menyimpan nilai 0
      result = 0
      # Selama current_node tidak none, maka valid
      while (current_node is not None):
        # Jika data dari node pertama modulus 2 == 0 / menghasilkan nilai genap
        if (current_node.data % 2 == 0):
          # Maka hasilnya 0
          count = 0
        # Jika menghasilkan nilai ganjil
        else:
          # Maka akan menampilkan data
          count = current_node.data
        # Akan menambah disetiap perulangannya
        result += count
        # Ke node selanjutnya
        current_node = current_node.next
      # Mengembalikan nilai
      return result
  
  def get_max(self):
    # Menginisialisasi variabel current_node sama dengan node pertama di dalam list yaitu head.
    current_node = self.head
    # Jika kosong
    if current_node is None:
      # Maka akan mengembalikan nilai none
      return None
    # Jika tidak kosong
    else:
      # Menginisialisasi variabel bilangan_maximal sama dengan data dari node pertama
      bilangan_maximal = current_node.data
      # Selama current_node tidak none, maka valid
      while(current_node is not None):
        # Jika data dari node pertama lebih dari bilangan_maximal
        if (current_node.data > bilangan_maximal):
          # Memanggil data
          bilangan_maximal = current_node.data
        # Ke node selanjutnya, sampai mendapatkan data nilai tertinggi
        current_node = current_node.next
      # Mengembalikan nilai
      return bilangan_maximal

# ==============================================================================
# ==============================================================================

# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya.
# Cocokkan hasil pemanggilan fungsi dengan solusi  
# yang seharusnya.
def test():
  list1 = LinkedList()
  list1.add_last(1)
  list1.add_last(2)
  list1.add_last(3)
  list1.add_last(4)
  list1.add_last(5)
  print('list1 : ', end='')
  list1.cetak()
  r1 = list1.sum_odd()
  print(f"list1.sum_odd() = {r1} \t(solusi: 9)")
  r2 = list1.get_max()
  print(f"list1.get_max() = {r2} \t(solusi: 5)")
  print()

  list2 = LinkedList()
  list2.add_last(9)
  list2.add_last(9)
  list2.add_last(9)
  print('list2 : ', end='')
  list2.cetak()
  r1 = list2.sum_odd()
  print(f"list2.sum_odd() = {r1} \t(solusi: 27)")
  r2 = list2.get_max()
  print(f"list2.get_max() = {r2} \t(solusi: 9)")
  print()

  list3 = LinkedList()
  list3.add_last(6)
  list3.add_last(2)
  list3.add_last(8)
  list3.add_last(4)
  print('list3 : ', end='')
  list3.cetak()
  r1 = list3.sum_odd()
  print(f"list3.sum_odd() = {r1} \t(solusi: 0)")
  r2 = list3.get_max()
  print(f"list3.get_max() = {r2} \t(solusi: 8)")
  print()

  list4 = LinkedList()
  print('list4 : ', end='')
  list4.cetak()
  r1 = list4.sum_odd()
  print(f"list4.sum_odd() = {r1} \t(solusi: 0)")
  r2 = list4.get_max()
  print(f"list4.get_max() = {r2} \t(solusi: None)")
  print()

if __name__ == '__main__':
  test()