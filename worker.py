## administer, PS, packer, deliver, picker

class Worker:
    def __init__(self, names, one_barcodes, parts):
        self.worker_data = {one_barcode: (name, part) for name, one_barcode, part in zip(names, one_barcodes, parts)}


    def create_worker(self, name, one_barcode, part):
        if one_barcode in self.worker_data:
            print(f"해당직원의 원바코드 '{one_barcode}' 는 이미 존재합니다 생성불가")
        else:
            self.worker_data[one_barcode] = (name, part)

    def read_worker(self, one_barcode):
        return self.worker_data.get(one_barcode, None)

    def update_worker(self, name, one_barcode, part):
        if one_barcode in self.worker_data:
            self.worker_data[one_barcode] = (name, part)
        else:
            print(f"해당 직원의 원바코드 '{one_barcode}를 업데이트할수없습니다")

    def delete_worker(self, one_barcode):
        if one_barcode in self.worker_data:
            del self.worker_data[one_barcode]
        else:
            print(f"해당 직원의 원바코드 '{one_barcode}를 삭제할수없습니다")

# 예제 사용
workers = Worker(['아무개', '아무개2', "아무개3", "아무개4", "아무개5"], ['1', '2', '3', '4', '5'], ['Ps', 'Packer', "Administer", "Deliver", "Picker"])
print(workers.read_worker('1'))  # ('Jake', 'Engineering')
workers.create_worker('아무개6', '6', 'packer')
workers.update_worker('아무개7', '7', 'picker')
workers.delete_worker('2')