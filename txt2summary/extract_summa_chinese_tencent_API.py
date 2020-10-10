import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
try:
    cred = credential.Credential("Input_ID", "Input_KEY")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "nlp.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

    req = models.AutoSummarizationRequest()
    params = {
        "Length": 100,
        "Text": """编程语言原本设计是专用于计算机，也用来定义算法或者数据结构。故而程序员试图使程序代码容易阅读。
        BBC BASIC语言显示在屏幕上
        编程语言往往使程序员能够比使用机器语言更准确地表达他们所想表达的目的。对那些从事计算机科学的人来说，懂得程序设计语言是十分重要的，因为在当今所有的计算都需要程序设计语言才能完成。

    目前发明了许多的编程语言，编程语言本身可能修改以符合新需求，或是和其他的编程语言结合使用，尽管人们多次试图创造可以符合所有需求的通用编程语言，但以“符合所有需求”的标准来看，这些尝试都失败了[来源请求]。之所以有那么多种不同的编程语言存在的原因是，编写程序的初衷其实也各不相同；新手与老手之间技术的差距非常小，而且有许多语言对新手来说太容易学；还有，不同程序之间的运行成本（runtime cost）各不相同。

    有许多用于特殊用途的语言，只在特殊情况下使用。例如，PHP专门用来显示网页；Perl适合文本处理；C语言被广泛用于操作系统和编译器的开发（所谓的系统编程）。[3]

    高级语言的出现使得计算机程序设计语言不再过度地依赖某种特定的机器或环境。这是因为高级语言在不同的平台上会被编译成不同的机器语言，而不是直接被机器执行。最早出现的编程语言FORTRAN的一个主要目标，就是实现平台独立。

    虽然大多数的语言既可被编译又可被解译，但大多数仅在一种情况下能够良好运行。在一些编程系统中，程序要经过几个阶段的编译，一般而言，后阶段的编译往往更接近机器语言。这种常用的使用技巧最早在1960年代末用于BCPL，编译程序先编译一个叫做“0代码”的转换程序（representation），然后再使用虚拟器转换到可以运行于机器上的真实代码。这种成功的技巧之后又用于Pascal和P-code，以及Smalltalk和二进制码，在很多时候，中间过渡的代码往往是解译，而不是编译的。

    如果所使用的翻译的机制是将所要翻译的程序代码作为一个整体翻译，并之后运行内部格式，那么这个翻译过程就被称为编译。因此，一个编译器是一个将人可阅读的程序文本（叫做源代码）作为输入的数据，然后输出可执行文件（object code）。所输出的可执行文件可以是机器语言，由计算机的中央处理器直接运行，或者是某种模拟器的二进制代码。

    如果程序代码是在运行时才即时翻译，那么这种翻译机制就被称作直译。经直译的程序运行速度往往比编译的程序慢，但往往更具灵活性，因为它们能够与执行环境互相作用。"""
    }
    req.from_json_string(json.dumps(params))

    resp = client.AutoSummarization(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)