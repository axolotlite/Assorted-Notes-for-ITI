Layers are shareable components used to create images.
These layers are cached to speed up building.
```
Only the instructions RUN, COPY, and ADD create layers. Other instructions create temporary intermediate images and do not increase the size of the build. We will see in the next section what these instructions are.
```