---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 773
evidence_level: L5
indication_count: 5
---

# Rosuvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Rosuvastatin：從血脂異常治療到膽固醇酯轉運蛋白缺乏症

## 一句話總結

Rosuvastatin 是 HMG-CoA 還原酶抑制劑（statin），文獻指出它用於治療血脂異常。
TxGNN 模型預測它可能對**膽固醇酯轉運蛋白缺乏症 (Cholesterol-ester transfer protein deficiency)** 有效。
目前**沒有臨床試驗**，只有 **2 篇文獻**，且都是其他脂蛋白疾病的病例報告，沒有直接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明（文獻指出用於血脂異常） |
| 預測新適應症 | 膽固醇酯轉運蛋白缺乏症 (Cholesterol-ester transfer protein deficiency) |
| TxGNN 預測分數 | 99.54% |
| 證據等級 | L5（證據包原先標為 L4，但檢索到的文獻都不涉及 rosuvastatin，故以僅有模型預測判定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Rosuvastatin 屬於 statin 類，已知透過抑制肝臟 HMG-CoA 還原酶來降低 LDL-C，這對一般血脂異常在機轉上說得通。

但是，CETP 缺乏症的特徵是 HDL-C 升高，並不是典型由 LDL 驅動的疾病。降 LDL-C 的機轉能否轉化為這個疾病的臨床益處，目前沒有資料支持。

檢索到的兩篇文獻分別談 Apo AI 缺乏症和肝脂肪酶缺乏症，都是其他原發性脂蛋白疾病，與 rosuvastatin 用於 CETP 缺乏症無關。0.995 的 TxGNN 分數只是模型預測，沒有直接的臨床支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | 病例報告／回顧 | Journal of Clinical Lipidology | 伊拉克曼達安族家庭完全 Apo AI 缺乏症，兩名同型合子患者臨床表現差異大；未涉及 rosuvastatin |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | 病例報告 | BMJ Case Reports | 中東阿拉伯裔男性肝脂肪酶缺乏症，首度報告此族群的 CETP 活性與質量；未涉及 rosuvastatin |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65620 | ROSETOR 5 TABLETS 5MG | 未載明 | 未載明 |
| HK-65073 | VICKROSTOR TABLETS 10MG | 未載明 | 未載明 |
| HK-64427 | ROSUVASTATIN ALVOGEN TABLETS 20MG | 未載明 | 未載明 |
| HK-61457 | APO-ROSUVASTATIN TABLET 20MG | 未載明 | 未載明 |
| HK-61936 | PMS-ROSUVASTATIN TABLETS 10MG | 未載明 | 未載明 |

共 20 張許可證，上表列出 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測目前只有模型分數，沒有任何臨床試驗，文獻也沒有直接涉及 rosuvastatin 與 CETP 缺乏症。
- CETP 缺乏症以 HDL-C 升高為特徵，並非典型的 LDL 驅動疾病，機轉上的連結很薄弱。

**若要推進需要：**
- 找到 rosuvastatin 用於 CETP 缺乏症的直接臨床或機轉研究。
- 取得香港衛生署的仿單內容，補齊核准適應症、警語與禁忌症。
- 取得 DrugBank 的作用機轉資料，以便進一步分析機轉關聯。
- 同一份資料中，**家族性高膽固醇血症**（預測排名第 2，L1，有多個 Phase 3 試驗，含兒童 HoFH 的 rosuvastatin 隨機對照試驗）證據明顯較強，但很可能屬於既有適應症。建議另案評估，並先確認本地仿單的適應症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

