# coding:utf-8
import subprocess, os


def get_filename():
    with open("images.txt", "r") as f:
        lines = f.read().split('\n')
        # print(lines)
        return lines

def pull_image():
    name_list = get_filename()
    for name in name_list:
        if name.strip() == "":
            continue
        print(" - name: %s" % name)
        if 'sha256' in name:
            sha256_name = name.split("@")
            new_name = sha256_name[0].split("/")[-1]
            tag = sha256_name[-1].split(":")[-1][0:6]
            print("   newName: wxzhang/%s" % new_name)
            print("   newTag: \"%s\"" % tag)
            # image = "wxzhang/" + new_name + ":" + tag
            # cmd = "docker tag {0}   {1}".format(name, image)
            # subprocess.call("docker pull {}".format(name), shell=True)
            # subprocess.run(["docker", "tag", name, image])
            # subprocess.call("docker login -u wxzhang -p qwer1234qwer", shell=True)
            # subprocess.call("docker push {}".format(image), shell=True)
        else:
            tmp = name.split("/")[-1].split(':')
            new_name = tmp[0]
            tag = tmp[1]
            print("   newName: wxzhang/%s" % new_name)
            print("   newTag: \"%s\"" % tag)
            # new_name = "wxzhang/" + name.split("/")[-1]
            # cmd = "docker tag {0}   {1}".format(name, new_name)
            # subprocess.call("docker pull {}".format(name), shell=True)
            # subprocess.run(["docker", "tag", name, new_name])
            # subprocess.call("docker login -u wxzhang -p qwer1234qwer", shell=True)
            # subprocess.call("docker push {}".format(new_name), shell=True)


if __name__ == "__main__":
    pull_image()
