# nginx에 가장 최근 버전을 다운로드 한다.
FROM nginx:latest

# nginx를 다운로드하면 기본 설정이 다음 경로에 생성된다.
# 기본 설정 내용을 삭제하고 django에서 만든 내용을 사용하기 위해 삭제작업 수행한다.
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d