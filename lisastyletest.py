class DiskTest:
    def run(self):
        print("Running disk test...")
        result = self.check_disk()
        if result:
            print("Disk test passed")
        else:
            raise Exception("Disk test failed")

    def check_disk(self):
        return True  # simulate success

test = DiskTest()
test.run()
