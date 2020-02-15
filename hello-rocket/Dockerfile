FROM rust:1.41
RUN rustup override set nightly

WORKDIR /usr/src/hello-rocket
COPY . .

RUN cargo install --path .

CMD ["hello-rocket"]
