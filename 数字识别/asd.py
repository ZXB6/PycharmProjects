import sensor, image, time, os, tf
sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

mobilenet_version = "1" # 1
mobilenet_width = "0.5" # 1.0, 0.75, 0.50, 0.25
mobilenet_resolution = "128" # 224, 192, 160, 128

mobilenet = "mobilenet_v%s_%s_%s_quant.tflite" % (mobilenet_version, mobilenet_width, mobilenet_resolution)
labels = [line.rstrip('\n') for line in open("mobilenet_labels.txt")]

clock = time.clock()
while(True):
    clock.tick()
    img = sensor.snapshot()
    for obj in tf.classify(mobilenet, img, min_scale=1.0, scale_mul=0.5, x_overlap=-1, y_overlap=-1):
        print("**********\nTop 5 Detections at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())
        sorted_list = sorted(zip(labels, obj.output()), key = lambda x: x[1], reverse = True)
        for i in range(5):
            print("%s = %f" % (sorted_list[i][0], sorted_list[i][1]))
    print(clock.fps(), "fps")