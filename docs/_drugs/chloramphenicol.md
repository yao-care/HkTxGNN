---
layout: default
title: Chloramphenicol
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-03
monitor_inn: "CHLORAMPHENICOL"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
description: "Chloramphenicol：預測新適應症為瀰漫性硬皮症 (diffuse scleroderma)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Chloramphenicol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Chloramphenicol: 瀰漫性硬皮症 (diffuse scleroderma)
{: .text-alpha }

## 一句話總結

Chloramphenicol（氯黴素）是一種抗菌藥，在香港以眼用與耳用製劑為主上市。
TxGNN 模型預測它可能對**瀰漫性硬皮症 (diffuse scleroderma)** 有效，但目前**沒有任何臨床試驗**，僅有 4 篇與硬皮症纖維母細胞機轉相關的體外研究，且這些研究並未測試氯黴素本身，證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 瀰漫性硬皮症 (diffuse scleroderma) |
| TxGNN 預測分數 | 0.9965 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 31 張／共 31 張） |
| 許可證數 | 31 張（有效 31 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。氯黴素一般認為是細菌核糖體抑制劑，主要作用於細菌蛋白質合成，與硬皮症的纖維化與自體免疫病理沒有明確的藥理連結。

檢索到的 4 篇文獻都是硬皮症纖維母細胞中第一型前膠原基因（COL1A1）轉錄調控與 TGF-β/Smad 訊息傳遞的基礎研究。標題顯示它們探討的是疾病生物學，並未把氯黴素當作治療藥物來測試。這些文獻可能因為實驗中使用了含氯黴素的報告基因系統而被檢索到，較像方法學上的巧合，並非藥理訊號。

因此，模型分數雖高，卻缺乏治療上的合理依據。氯黴素已知有骨髓抑制毒性，用於慢性自體免疫疾病並不理想。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | 體外機轉研究 | Rheumatology (Oxford) | 探討 TGF-β/Smad 訊息在硬皮症纖維母細胞膠原基因表現增加中的角色，涉及 Smad3 與 Sp1、p300 的交互作用 |
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | 體外機轉研究 | Arthritis Rheum | 阻斷內源性 TGF-β 訊息可抑制硬皮症纖維母細胞中膠原合成上調 |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | 體外機轉研究 | Arthritis Rheum | 找出第一型前膠原基因啟動子區中與系統性硬化症上調表現有關的調控元件 |
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | 體外機轉研究 | Arthritis Rheum | 研究瀰漫性系統性硬化症皮膚纖維母細胞中 COL1A1 的轉錄活化與內含子序列的角色 |

以上文獻均未評估氯黴素對硬皮症的療效。

## 香港上市資訊

香港共有 31 張含本藥成分的許可證（全部有效；單一成分 18 張、複方 13 張）。以下列出其中 5 張：

<!-- review:begin hk-lic-20261117-chloramphenicol-1 -->

> **查核更正（2026-11-17）**：原文為「氯黴素在香港有 20 張有效的單一成分許可證，沒有已註銷者。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 31 張含本藥成分的許可證（全部有效；單一成分 18 張、複方 13 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-chloramphenicol-1 -->

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61895 | EUROPHEN EYE DROPS 0.5%W/V | 眼藥水（依品名） | 未載明 |
| HK-61645 | VANAFEN OPHTHALMIC OINTMENT 1% W/W | 眼用軟膏（依品名） | 未載明 |
| HK-09064 | CHLORAMPHENICOL EYE DROPS 0.5% (FAMAR S.A.) | 眼藥水（依品名） | 未載明 |
| HK-01687 | CHLORAMPHENICOL EAR DROPS 5% | 耳滴劑（依品名） | 未載明 |
| HK-30632 | DEXMIN EYE/EAR DROPS | 眼／耳滴劑（依品名） | 未載明 |

## 安全性考量

- **血液毒性**：氯黴素已知有骨髓抑制毒性，這是用於慢性疾病的主要障礙。
- **藥物交互作用**：已查得多項交互作用，較重要的如下。
  - **重大 (Major)**：Cisapride、Naloxegol
  - **中度 (Moderate)**：Aprepitant、Balsalazide、Metronidazole、Budesonide、Iron、Eliglustat、Naldemedine、Nitisinone
  - **降血糖藥（中度）**：Acetohexamide、Chlorpropamide、Glimepiride、Glipizide、Glyburide、Repaglinide、Saxagliptin
  - **降血脂藥（中度）**：Rosuvastatin、Simvastatin

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，唯一的文獻是不涉及氯黴素的體外機轉研究，證據等級僅為 L5。
- 氯黴素的抗菌機轉與硬皮症病理缺乏連結，且骨髓抑制風險高，不適合長期使用。

**若要推進需要：**
- 取得氯黴素的詳細作用機轉資料，並說明其與纖維化路徑的可能連結
- 以體外或動物模型直接檢驗氯黴素對硬皮症纖維母細胞膠原表現的影響
- 取得完整的仿單警語與禁忌症資料，進行安全性評估
- 若前臨床結果有利，再評估血液毒性監測方案與給藥途徑的可行性

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「氯黴素在香港有 20 張有效的單一成分許可證，沒有已註銷者。」→「香港共有 31 張含本藥成分的許可證（全部有效；單一成分 1」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

