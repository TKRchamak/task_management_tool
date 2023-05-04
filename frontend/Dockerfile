# ==== CONFIGURE =====
# Use a Node 16 base image
FROM node:16-alpine 

# Set the env to "production"
ENV NODE_ENV develpoment

# Set the working directory to /app inside the container
WORKDIR /app
# Copy app files
COPY . .
# Install dependencies (npm ci makes sure the exact versions in the lockfile gets installed)
RUN yarn install

# ==== BUILD =====
# Build the app
# RUN npm run build

# ==== RUN =======
# Expose the port on which the app will be running (3000 is the default that `serve` uses)
EXPOSE 3000

# Start the app
CMD [ "yarn", "start" ]