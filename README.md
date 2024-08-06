# 深度学习在生物医药领域的应用

一个持续更新的专有领域知识库，聚焦深度学习技术在生物医药领域的具体应用，通过收集和整理最新科研文献提供信息。

---

## 动机

我曾在 [NCBI PubMed](https://pubmed.ncbi.nlm.nih.gov/) 订阅了关键词"deep learning" OR "convolutional neural networks"，每天会收到数十至数百篇相关文献的推送，内容繁多，涉猎广泛，且都与生物医药相关。2022年，我决定在快速浏览这些文献的同时，手工整理其信息，以便更系统地理解“深度学习在生物医药领域的应用”，然而，由于手工整理文献信息的工作量太大，这个项目并未进行多久便停滞了。两年后，大语言模型（LLM）迅速崛起，让自动化的文献整理和信息提取变得可能，本项目也作为一项尝试而重新继续。

## 如何使用

1. 克隆本仓库：

    ```sh
    git clone https://github.com/yanlinlin82/what-deep-learning-does-in-biomedicine.git
    ```

2. 准备环境

    ```sh
    python -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    ```

3. 配置环境参数

    ```sh
    vi .env
    ```

    ```txt
    OPENAI_BASE_URL=https://api.deepseek.com  # 若使用 openai API，则留空，或使用 https://api.openai.com/v1
    OPENAI_API_KEY=sk-XXXX                    # 填写自己账号的 API Key
    OPENAI_MODEL=deepseek-chat                # 若使用 openai API，可设置为 gpt-4o-mini
    OPENAI_PROXY_URL=socks5://x.x.x.x:xxxx    # 用于（从国内翻墙）调用 openai API，使用 DeepSeek 则可不配置此项
    ```
  
4. 初始化并运行Django

    ```sh
    python manage.py migrate
    python manage.py collectstatic
    ```

5. PubMed数据获取

    ```sh
    lftp -c "mirror -c https://ftp.ncbi.nlm.nih.gov/pubmed/" # 注意全套下载有超过50G
    ```

6. 扫描PubMed文件，提取文献信息，导入数据库

    ```sh
    python scripts/scan-pubmed.py /path/to/pubmed/updatefiles/pubmed24nXXXX.xml.gz
    python scripts/import.py output/
    ```

## 免责声明

本项目信息由手工或AI整理，信息难免存在错漏，请使用时务必注意核实。此外，由于各种原因，项目可能会不定期断档停更，还请见谅！

## 许可证

本仓库基于 [MIT协议](LICENSE) 发布，允许自由修改和传播。
