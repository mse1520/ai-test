# AI Test
ai와 관련된 테스트 및 예제 소스입니다.
- [Python 기본 사용법](./docs/python.md)
- [용어 정리](./docs/ai.md)

## 개발 초기 설정

### GPU 설정
ai 모델 학습에는 CPU보다 `GPU`를 썼을 때 더 빠른 시간 내에 학습을 마칠 수 있기에 `GPU`를 써서 훈련하는 초기 설정을 해야 합니다.  
다음의 가이드는 `Windows` os와 `RTX 3050` 그래픽카드, `torch 2.0.1`을 기준으로 작성되었습니다.

1. Pytorch를 사용할 것이기 때문에 [Pytorch 문서](https://pytorch.org/)에서 Pytorch 버전에 맞는 `CUDA 버전을 확인`합니다.
2. 확인된 버전의 CUDA를 검색하여 설치합니다. [CUDA Toolkit 11.7](https://developer.nvidia.com/cuda-11-7-0-download-archive)
3. cuDNN를 다운([링크](https://developer.nvidia.com/cudnn))받고 `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7` 경로에 다운받은 `bin, include, lib` 폴더를 옮깁니다.
4. [Pytorch 문서](https://pytorch.org/)를 참고하여 Pytorch를 설치합니다.
4. 다음의 코드를 실행해서 Pytorch가 정상적으로 GPU를 사용해서 실행하는지 확인힙니다.
```python
import torch
print(torch.cuda.is_available())
```