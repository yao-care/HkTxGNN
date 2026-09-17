---
layout: default
title: Nystatin
parent: 高證據等級 (L1-L2)
nav_order: 534
evidence_level: L2
indication_count: 5
---

# Nystatin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Nystatin：從念珠菌感染到外陰陰道炎

## 一句話總結

Nystatin 是一種多烯類（polyene）大環內酯抗真菌藥，傳統用於治療念珠菌感染，但目前在香港**未上市**，無正式核准適應症紀錄。
TxGNN 模型預測它對**外陰陰道炎 (Vulvovaginitis)** 有效，目前有 **0 個臨床試驗**登記，但有 **20 篇文獻**支持這個方向，其中多篇直接研究 nystatin 用於念珠菌性外陰陰道炎。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 念珠菌感染（抗真菌用途；香港未上市，無正式核准適應症紀錄） |
| 預測新適應症 | 外陰陰道炎 (Vulvovaginitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Nystatin 是多烯類大環內酯抗真菌藥，與真菌細胞膜上的 ergosterol 結合形成孔洞，導致細胞內容物滲漏、真菌死亡。目前缺乏 DrugBank 完整 MOA 條目，但此機轉描述已可從證據包的再利用推論中確認。

念珠菌性外陰陰道炎（vulvovaginal candidiasis, VVC）的致病原正是 *Candida* spp.，與 nystatin 的抗真菌機轉直接對應。事實上，這並非單純模型憑空關聯，而是 nystatin 全球行之有年的傳統用途之一（陰道用製劑治療念珠菌性陰道炎）——只是在香港目前尚未取得許可證上市。因此本案性質上更接近「已知療效藥物的在地化上市評估」，而非全新機轉假說。

多篇文獻（如陰道 nystatin 體外藥敏與臨床療效相關性研究、大鼠模型免疫調節研究）也從不同角度支持其在 VVC 治療上的生物學合理性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | 抗氟康唑外陰陰道念珠菌病現行治療進展，涵蓋 nystatin 等替代抗真菌療法 |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Cohort | Ceska gynekologie | 陰道 nystatin + nifuratel 併用治療混合型外陰陰道炎的療效評估 |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Cohort | Mycoses | 287 例複雜性外陰陰道念珠菌病之 nystatin 體外藥敏與臨床療效相關性分析 |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | 機轉研究 | BMC Microbiology | 大鼠模型顯示 nystatin 可增強抗念珠菌免疫反應並保護陰道上皮超微結構 |
| [37023426](https://pubmed.ncbi.nlm.nih.gov/37023426/) | 2023 | 比較研究 | J Infect Dev Ctries | 比較茶樹油與 nystatin 對孕婦陰道念珠菌分離株的抑菌圈效果 |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | 實驗研究 | Infect Drug Resist | ZnO 奈米粒子與 nystatin 對氟康唑抗藥性念珠菌 SAP1-3 基因表現之抑制作用 |
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Review | BMJ Clinical Evidence | 外陰陰道念珠菌病為僅次於細菌性陰道炎的常見陰道炎病因總論 |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Review | J Women's Health | 硼酸用於復發性外陰陰道念珠菌病之臨床證據回顧（含與 nystatin 比較） |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | 外陰陰道念珠菌病臨床總論 |
| [8624598](https://pubmed.ncbi.nlm.nih.gov/8624598/) | 1996 | Cohort | Ceska gynekologie | 兒童與青少年混合病因外陰陰道炎之 nifuratel + nystatin 併用治療 |

## 香港上市資訊

目前尚未於香港取得藥品許可證（0 張登記）。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Vulvovaginitis（念珠菌性）屬 nystatin 的傳統已知適應症，機轉直接針對病原體 *Candida*，並有多篇體外藥敏、世代研究與機轉研究佐證，證據等級達 L2；但目前無 RCT 等級證據，且香港未上市、仿單警語與完整 MOA 資料均缺失，需在防護措施下推進。

**若要推進需要：**
- 補齊香港（或參考 TFDA）仿單警語與禁忌症資料（Blocking，DG001）
- 補齊 DrugBank 完整作用機轉資料（High，DG002）
- 若擬在香港上市，需準備完整藥品註冊申請（目前 0 張許可證）
- 規劃前瞻性 RCT 驗證陰道用 nystatin 對外陰陰道念珠菌病的療效與安全性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

