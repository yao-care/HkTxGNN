---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 3
---

# Doravirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Doravirine：從 HIV-1 感染 到 猴免疫缺乏病毒感染

## 一句話總結

Doravirine 是一種非核苷類逆轉錄酶抑制劑（NNRTI），原本用於 HIV-1 感染的抗病毒治療。
TxGNN 模型預測它可能對**猴免疫缺乏病毒感染（Simian Immunodeficiency Virus Infection）** 有效，
目前有 **0 個臨床試驗**及 **1 篇間接相關文獻**，整體證據極為薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（NNRTI 類抗病毒藥物） |
| 預測新適應症 | 猴免疫缺乏病毒感染（Simian Immunodeficiency Virus Infection） |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Doravirine 屬於 NNRTI（非核苷類逆轉錄酶抑制劑）類別，透過非競爭性結合 HIV-1 逆轉錄酶上的 NNRTI 結合口袋（NNRTI binding pocket），抑制病毒 RNA 轉換為 DNA 的過程，從而阻斷 HIV-1 複製。

SIV（猴免疫缺乏病毒）與 HIV-1 同屬慢病毒屬（Lentivirus），均依賴逆轉錄酶進行複製——這正是 TxGNN 知識圖譜中兩者節點高度相似、模型給出近滿分的根本原因。

然而，此預測存在**明確的藥理障礙**：SIV 逆轉錄酶的 NNRTI 結合口袋與 HIV-1 RT 在關鍵殘基上差異顯著（Y181、Y188、W229 等位點結構不同），已有生化研究確認現有 NNRTIs 對 SIV RT 的抑制活性極低。**模型高分反映的是知識圖譜拓撲相似性，而非實際藥理活性，不宜直接詮釋為臨床再利用的支持依據。**

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | 探討 islatravir（逆轉錄酶易位抑制劑，RTTI）用於 HIV-1 治療與預防之潛力；主角為 islatravir 而非 Doravirine，與本預測適應症（SIV）無直接關聯 |

> ⚠️ 此篇文獻討論對象為另一種逆轉錄酶抑制劑（islatravir），且針對 HIV-1 而非 SIV，相關性極為有限，不構成對本預測的支持證據。

---

## 香港上市資訊

Doravirine 目前在香港尚未取得藥品許可證，無任何上市記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
三項預測適應症（SIV 感染、貓後天免疫缺乏症候群、罕見神經發育障礙）均為 L5 等級，且最高排名的 SIV 感染預測存在明確的反向藥理障礙——NNRTIs 對 SIV 逆轉錄酶的抑制活性極低，高預測分數源自知識圖譜拓撲相似性而非真實藥理相關性，在現有知識框架下不具再利用價值。

**若要推進需要：**
- 補充 Doravirine 完整 MOA 及 NNRTI binding pocket 與 SIV/FIV RT 的序列比對資料，確認結合口袋差異程度
- 取得原廠仿單的完整警語與禁忌資訊（目前為 Data Gap）
- 若考慮第三項適應症（神經發育障礙），需先進行 NNRTI 抑制內源性 LINE-1 逆轉錄元素活性的前臨床 PoC 實驗
- 評估 TxGNN 模型是否對 HIV 相關病毒節點產生系統性過度預測偏差，並考慮在知識圖譜中加入跨物種 NNRTI 結合口袋相似性的邊權重修正
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

