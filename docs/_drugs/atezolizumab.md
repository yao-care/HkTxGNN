---
layout: default
title: Atezolizumab
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
---

# Atezolizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Atezolizumab：從原適應症（資料未載明）到攝護腺尿道泌尿上皮癌

## 一句話總結

Atezolizumab 是抗 PD-L1 的單株抗體，香港已有 3 張許可證，但輸入資料未載明原適應症。
TxGNN 模型預測它可能對**攝護腺尿道泌尿上皮癌 (Prostatic Urethra Urothelial Carcinoma)** 有效。
目前有 **2 個臨床試驗**（1 個 Phase 2、1 個 Phase 1b），**沒有相關文獻**，且都不是專門針對攝護腺尿道的研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 攝護腺尿道泌尿上皮癌 (Prostatic Urethra Urothelial Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2（寬鬆判定，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

> **證據等級說明**：L2 的判定來自一項已完成的 Phase 2 試驗，但該試驗看起來是單臂、非隨機設計，並非嚴格定義的 RCT，因此屬於寬鬆判定。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Atezolizumab 是抗 PD-L1 的免疫檢查點抑制劑，能解除腫瘤對 T 細胞的抑制，恢復抗腫瘤免疫反應。

泌尿上皮癌常表現 PD-L1。攝護腺尿道是泌尿上皮癌可能出現的部位之一，與膀胱泌尿上皮癌屬於同一疾病家族。因此從機轉上推論，PD-L1 阻斷可能適用於此部位。

不過，現有的 Phase 2 證據來自「卡介苗 (BCG) 無反應的非肌肉侵犯性膀胱癌」，並非攝護腺尿道的專屬族群。此外，Atezolizumab 在泌尿上皮癌的既有核准狀態，輸入資料沒有記載，需另行查證。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02844816](https://clinicaltrials.gov/study/NCT02844816) | Phase 2 | 完成 | 172 | Atezolizumab 用於 BCG 無反應的復發性非肌肉侵犯性膀胱癌。疾病屬同一家族但部位不同，攝護腺尿道是否為獨立亞群尚不明確（相關性 B） |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1b | 進行中（已停止收案） | 914 | Cabozantinib 單用或併用 Atezolizumab，涵蓋多種晚期實體瘤（含泌尿上皮癌）。這是劑量探索與安全性研究，併用設計無法歸因於 Atezolizumab 單藥（相關性 C） |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66613 | TECENTRIQ CONCENTRATE FOR SOLUTION FOR INFUSION 840MG/14ML | ROCHE HONG KONG LIMITED |
| HK-66341 | TECENTRIQ CONCENTRATE FOR SOLUTION FOR INFUSION 1200MG/20ML | ROCHE HONG KONG LIMITED |
| HK-65567 | TECENTRIQ CONCENTRATE FOR SOLUTION FOR INFUSION 1200MG/20ML | ROCHE HONG KONG LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（抗 PD-L1 單株抗體） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 對攝護腺尿道這個特定部位，目前只有間接證據：一項來自膀胱癌的單臂 Phase 2，以及一項多腫瘤的 Phase 1b 併用研究，沒有專屬的試驗或文獻。
- 香港仿單的警語與禁忌症資料缺口屬於阻斷性 (Blocking)，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症，並確認現有核准適應症（特別是泌尿上皮癌）
- 補充作用機轉資料（可查詢 DrugBank）
- 檢視 NCT02844816 是否有攝護腺尿道受侵的亞群分析
- 搜尋攝護腺尿道或上泌尿道泌尿上皮癌的專屬文獻與試驗

**其他預測適應症備註：** 「子宮內頸癌 (Endocervical Carcinoma)」也達到 L2，有 2 個已完成的早期試驗（NCT02921269 為 n=11 的 Phase 2，NCT03738228 為 n=40 的 Phase 1）。其餘預測適應症目前僅有模型預測（L5），建議維持 Hold。

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

