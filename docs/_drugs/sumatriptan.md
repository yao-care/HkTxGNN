---
layout: default
title: Sumatriptan
parent: 中證據等級 (L3-L4)
nav_order: 715
evidence_level: L4
indication_count: 1
---

# Sumatriptan
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Sumatriptan：從偏頭痛到腦幹先兆偏頭痛

## 一句話總結

Sumatriptan 是廣泛使用的 5-HT1B/1D 受體促效劑，目前香港未上市、無許可證資料可查。
TxGNN 模型預測它對**腦幹先兆偏頭痛 (Migraine with Brainstem Aura)** 有效，
但目前**無臨床試驗**支持，僅有 **20 篇文獻**，且機轉分析顯示此適應症在臨床上可能屬於**相對或絕對禁忌**，而非可推進的新用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 港無許可證資料（未上市，無法從登記資料確認） |
| 預測新適應症 | 腦幹先兆偏頭痛 (Migraine with Brainstem Aura) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L4 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？（附重要警示）

Sumatriptan 是選擇性 5-HT1B/1D 受體促效劑，作用機轉為收縮特定腦血管、並抑制三叉神經血管系統釋放發炎性神經胜肽，這是它治療一般偏頭痛的核心機轉。

腦幹先兆偏頭痛（舊稱「基底型偏頭痛」）在疾病分類上仍屬偏頭痛家族的亞型，理論上與一般偏頭痛共享相同的三叉神經血管發炎路徑，這可能是 TxGNN 模型將兩者關聯起來、給出高分預測的原因。

**但需特別注意**：此亞型的先兆症狀源自腦幹或椎基底動脈循環系統的功能異常，而 triptan 類藥物具有血管收縮作用，理論上存在加重腦幹缺血的風險。因此在多數國際偏頭痛治療指引與藥品仿單中，**腦幹先兆偏頭痛被列為 triptan 類藥物的相對或絕對禁忌症**。也就是說，模型基於「同屬偏頭痛」的廣泛關聯給出高分，但未能捕捉到這個亞型在臨床安全性上的特殊限制——機轉關聯與安全性建議方向相反。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

檢視現有 20 篇文獻後發現，**沒有任何一篇是專門針對「腦幹先兆偏頭痛」這個亞型**進行的研究，多數是一般偏頭痛或「有先兆偏頭痛」的研究。以下列出證據等級較高、與先兆/安全性最相關的文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | 美國頭痛學會對偏頭痛急性藥物療效的實證評估 |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort/Comparative | Neurology | Sumatriptan 在「有先兆」偏頭痛的療效低於「無先兆」偏頭痛 |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | 雙盲安慰劑對照試驗，評估口服 sumatriptan 治療有先兆偏頭痛之療效 |
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | Cephalalgia | 早期投藥 sumatriptan 可預防 PACAP38 誘發之偏頭痛發作 |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytotherapy Research | 薑粉與 sumatriptan 治療一般偏頭痛之療效比較 |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Mechanistic/PET study | JAMA Neurology | 探討 sumatriptan 在偏頭痛發作時與中樞 5-HT1B 受體結合之關係 |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | 未分類 | Neurology | 皮下注射 sumatriptan 與偏頭痛先兆之關係 |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Sumatriptan 治療偏頭痛與叢集性頭痛之臨床經驗回顧 |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Expert Review | Expert Rev Neurother | Sumavel DosePro（無針皮下注射劑型）核准用於有無先兆之偏頭痛 |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook Clin Neurol | 偏頭痛重積狀態（status migrainosus）之併發症回顧 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉分析顯示 triptan 類藥物在腦幹先兆偏頭痛族群中，因血管收縮作用具理論性缺血風險，多數指引將其列為相對或絕對禁忌，與 TxGNN 高分預測方向相反。
- 證據等級僅 L4（機轉推論層級），無任何直接針對此亞型的臨床試驗，且香港未上市、無仿單警語與禁忌症資料可核對安全性（DG001，Blocking）。

**若要推進需要：**
- 補齊 TFDA/HK 仿單完整警語與禁忌症資料（對應 DG001）
- 取得完整 MOA 資料以確認機轉關聯性（對應 DG002）
- 若欲重新評估，需先有針對腦幹先兆偏頭痛族群的安全性研究，釐清現行禁忌是否仍適用於現代劑型/劑量
- 在安全性疑慮未解除前，本候選建議維持排除狀態，而非列為再利用機會
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

