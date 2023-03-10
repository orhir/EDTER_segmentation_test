ARG PYTORCH="1.6.0"
ARG CUDA="10.1"
ARG CUDNN="7"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0+PTX"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
RUN apt-get update && apt-get install -y git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install mmsegmentation
RUN conda clean --all
RUN pip install mmcv-full==latest+torch1.6.0+cu101 -f https://download.openmmlab.com/mmcv/dist/index.html
#RUN git@github.com:open-mmlab/mmsegmentation.git /mmsegmentation
#RUN git clone https://github.com/open-mmlab/mmsegmenation.git /mmsegmentation

# Install MMCV
ARG PYTORCH
ARG CUDA
ARG MMCV
RUN ["/bin/bash", "-c", "pip install --no-cache-dir mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu${CUDA//./}/torch${PYTORCH}/index.html"]


WORKDIR /storage/orhir

# # allows ssh to the docker from outside the container
# RUN sed 's@.*AuthorizedKeysFile.*@AuthorizedKeysFile /storage/orhir/.ssh/authorized_keys@' -i /etc/ssh/sshd_config
# RUN chmod 0700 /storage/orhir

# allows the docker to access the outside world:
RUN sed 's@.*IdentityFile.*@IdentityFile /storage/orhir/.ssh/id_ed25519@' -i /etc/ssh/ssh_config
RUN sed 's@.*StrictHostKeyChecking.*@StrictHostKeyChecking off@' -i /etc/ssh/ssh_config

# do not ask for git password
RUN sed 's@.*BatchMode.*@BatchMode yes@' -i /etc/ssh/ssh_config


# Install Repo
RUN git clone https://github.com/orhir/EDTER_segmentation_test.git
WORKDIR EDTER_segmentation_test/mmsegmentation/
ENV FORCE_CUDA="1"
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -e .

WORKDIR ../
# RUN ./tools/dist_train.sh configs/bsds/EDTER_BIMLA_320x320_80k_bsds_bs_4.py 2
