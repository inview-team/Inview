FROM node:lts-alpine
WORKDIR /home/Inview/frontend
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN cp -r /home/Inview/frontend/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]