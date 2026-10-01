---
layout: default
title: Orphenadrine
parent: 僅模型預測 (L5)
nav_order: 634
evidence_level: L5
indication_count: 7
---

# Orphenadrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Orphenadrine：從肌肉鬆弛（抗膽鹼藥）到視網膜失養症

## 一句話總結

Orphenadrine 是抗膽鹼（毒蕈鹼拮抗）類肌肉鬆弛藥，臨床上也用於改善抗精神病藥引起的帕金森症狀。
TxGNN 模型預測它可能對**視網膜失養症（retinal dystrophy with or without extraocular anomalies）**有效。
目前**無臨床試驗**，檢索到的 **16 篇文獻**都是眼科背景文獻，沒有一篇直接研究 orphenadrine，因此證據只有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 視網膜失養症（伴或不伴眼外異常） |
| TxGNN 預測分數 | 99.29% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知的藥理特性，orphenadrine 是抗膽鹼藥，同時具有 H1 抗組織胺與 NMDA 拮抗作用。

**機轉上看不出可信的關聯。** 遺傳性視網膜失養症是光受器或視網膜色素上皮的基因性退化。上述三條藥理路徑都不處理這類病因，0.993 的高分只是知識圖譜的推論結果，檢索到的證據無法支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻是以疾病關鍵字檢索到的，內容為眼部先天異常、眼外肌等背景知識，**都沒有評估 orphenadrine**，只能視為疾病背景參考，不構成藥物療效證據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | 複視的系統性評估方法與鑑別診斷 |
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | 眼眶感染多由鼻竇炎引起，臨床表現含眼球突出與眼球運動受限 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblatter fur Augenheilkunde | 先天性眼瞼下垂的分型、合併症與檢查重點 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | 水晶體大小、形狀與位置的先天異常 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | 兒童眼部病變的鑑別診斷與影像特徵 |
| [10192514](https://pubmed.ncbi.nlm.nih.gov/10192514/) | 1999 | Review | Progress in Retinal and Eye Research | 眼外肌本體感覺器與空間視覺知覺的角色 |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Review | Neuroradiology | 眼肌麻痺的神經影像與臨床特徵 |
| [37408430](https://pubmed.ncbi.nlm.nih.gov/37408430/) | 2023 | Review | 中華眼科雜誌 | 眼外肌結構與神經支配的研究進展 |
| [39582415](https://pubmed.ncbi.nlm.nih.gov/39582415/) | 2024 | Cohort | Birth Defects Research | 歐洲 15 國先天性眼部異常盛行率 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | 兩例單側隱眼畸形的臨床特徵 |

## 香港上市資訊

以下為主要 5 張許可證，資料中沒有劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-46326 | TENSIONLEX TAB 100MG | YAT SENG TRADING CO |
| HK-65487 | MANGA TABLETS | R. MANSTIEN (AUSTRALIA) LIMITED |
| HK-55766 | MYOFLEX TAB | LEAMYK INVESTMENT LIMITED |
| HK-62231 | JMP PARACETAMOL & ORPHENADRINE CITRATE TABLETS | SYNCO (H.K.) LIMITED |
| HK-19321 | NORGESIC TAB | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型分數，沒有臨床試驗，文獻也與藥物無關，機轉上也看不出關聯，證據等級為 L5。
- 視網膜失養症是基因性退化疾病，orphenadrine 的藥理作用不針對其病因。

**其他預測適應症：**
- 精神分裂症（rank 5）的證據較多，評為 L3。但文獻多半談的是 orphenadrine 用於改善抗精神病藥引起的錐體外症狀，不是治療精神病核心症狀。
- 抗膽鹼藥可能加重認知功能問題與遲發性運動障礙，安全性需要審慎評估。
- 其餘預測（醣基化異常、多小腳迴、CMT1G、近視）皆無試驗與文獻，同為 Hold。

**若要推進需要：**
- 補齊 DrugBank 作用機轉資料，並取得香港衛生署仿單的警語與禁忌症。
- 以機轉為基礎，做針對性的文獻與前臨床檢索，確認是否有直接證據。
- 若要優先探索，建議先從精神分裂症方向釐清其臨床意義，再決定是否推進。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

