class Worker:
    def __init__(self, names, barcodes, parts):
        self.worker_data = {barcode: (name, part) for name, barcode, part in zip(names, barcodes, parts)}

    def create_worker(self, name, barcode, part):
        if barcode in self.worker_data:
            print(f"Worker with barcode '{barcode}' already exists.")
        else:
            self.worker_data[barcode] = (name, part)

    def read_worker(self, barcode):
        return self.worker_data.get(barcode, None)

    def update_worker(self, name, barcode, part):
        if barcode in self.worker_data:
            self.worker_data[barcode] = (name, part)
        else:
            print(f"Worker with barcode '{barcode}' not found.")

    def delete_worker(self, barcode):
        if barcode in self.worker_data:
            del self.worker_data[barcode]
        else:
            print(f"Worker with barcode '{barcode}' not found.")

# 예제 사용
workers = Worker(['Jake', 'Amy'], ['1234', '5678'], ['Engineering', 'HR'])
print(workers.read_worker('1234'))  # ('Jake', 'Engineering')
workers.create_worker('Rosa', '9012', 'Security')
workers.update_worker('Terry', '5678', 'Marketing')
workers.delete_worker('1234')