FROM nginx:mainline-alpine

RUN rm /etc/nginx/conf.d/default.conf

# Copy configuration
COPY dhparam.pem /etc/nginx/
COPY snippets/ /etc/nginx/snippets/
COPY nginx.conf.template /etc/nginx/templates/