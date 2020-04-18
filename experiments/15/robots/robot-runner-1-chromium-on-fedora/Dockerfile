FROM fedora:30

# Setup volumes for input and output
VOLUME /opt/robotframework/reports
VOLUME /opt/robotframework/tests

# Setup X Window Virtual Framebuffer
ENV SCREEN_COLOUR_DEPTH 24
ENV SCREEN_HEIGHT 1080
ENV SCREEN_WIDTH 1920

# Dependency versions
ENV CHROMIUM_VERSION 72.0.*
ENV FIREFOX_VERSION 69.0.*
ENV GECKO_DRIVER_VERSION v0.26.0
ENV ROBOT_FRAMEWORK_VERSION 3.1.2
ENV SELENIUM_LIBRARY_VERSION 4.1.0

# Install system dependencies
RUN dnf upgrade -y \
  && dnf install -y \
    chromedriver \
    chromium  \
    firefox \
    xauth \
    xorg-x11-server-Xvfb \
    which \
    wget \
  && dnf clean all

# Install Robot Framework and Selenium Library
RUN pip3 install \
  requests==2.9 \
  robotframework==$ROBOT_FRAMEWORK_VERSION \
  robotframework-seleniumlibrary==$SELENIUM_LIBRARY_VERSION \
  robotframework-selenium2library \
  google-api-python-client \
  oauth2client

# Download Gecko drivers directly from the GitHub repository
RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz" \
      && tar xzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz \
      && mkdir /opt/robotframework/drivers/ \
      && mv geckodriver /opt/robotframework/drivers/geckodriver \
      && rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz

# Prepare binaries to be executed
COPY bin/chromedriver.sh /opt/robotframework/bin/chromedriver
COPY bin/chromium-browser.sh /opt/robotframework/bin/chromium-browser
COPY bin/run-tests-in-virtual-screen.sh /opt/robotframework/bin/

# FIXME: below is a workaround, as the path is ignored
RUN mv /usr/lib64/chromium-browser/chromium-browser /usr/lib64/chromium-browser/chromium-browser-original \
  && ln -sfv /opt/robotframework/bin/chromium-browser /usr/lib64/chromium-browser/chromium-browser

# Update system path
ENV PATH=/usr/local/bin:/opt/robotframework/bin:/opt/robotframework/drivers:$PATH
