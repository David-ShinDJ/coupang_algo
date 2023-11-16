import hashlib

def hash_name(name):
    # 이름을 바이트 문자열로 인코딩
    name_bytes = name.encode('utf-8')

    # hashlib 사용하여 SHA-256 해시 생성
    sha256_hash = hashlib.sha256(name_bytes)

    # 해시값을 16진수로 변환하여 반환
    return sha256_hash.hexdigest()[:14]