---
layout: default
title: Tolvaptan
parent: 高證據等級 (L1-L2)
nav_order: 757
evidence_level: L1
indication_count: 10
---

# Tolvaptan
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Tolvaptan：原適應症資料缺失，聚焦體染色體顯性多囊腎病（合併多囊肝病）

## 一句話總結

Tolvaptan 目前香港無許可證登記（未上市），且原始核准適應症與正式作用機轉資料皆缺失。
TxGNN 模型預測分數最高的適應症是**體染色體顯性多囊腎病 3 型合併/不合併多囊肝病**，
目前資料庫中無登記臨床試驗記錄，但有 **20 篇文獻**支持，其中包含 2 項關鍵性 Phase 3 RCT（TEMPO 3:4、REPRISE）。值得注意的是，此適應症在國際上（FDA/EMA）已是正式核准用途，並非單純的模型外推。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（DrugBank 與香港許可證均無記錄，見 DG002） |
| 預測新適應症 | 體染色體顯性多囊腎病 3 型合併/不合併多囊肝病 (Polycystic Kidney Disease 3 with or without Polycystic Liver Disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏正式的 DrugBank 作用機轉摘要，香港也無許可證與原適應症紀錄可供比對（DG001、DG002 為阻斷性/高優先級資料缺口）。不過，evidence pack 內建的機轉分析明確指出：Tolvaptan 為選擇性血管加壓素 V2 受體（V2 receptor）拮抗劑，可阻斷腎集合管的 V2R–cAMP 訊號路徑。

這條路徑正是體染色體顯性多囊腎病（ADPKD）囊腫生長與液體分泌的關鍵驅動因子。因此，此適應症在國際上（FDA/EMA）事實上已經是 Tolvaptan 的正式核准用途，並非單純的模型推測——TxGNN 給出的近乎滿分預測（99.99%）與既有的兩項 Phase 3 RCT（TEMPO 3:4、REPRISE）高度吻合。

多囊肝病是 ADPKD 最常見的腎外表現，兩者共享類似的纖毛蛋白/囊腫形成機轉，這也是預測疾病名稱同時涵蓋「合併多囊肝病」的原因。但針對多囊肝病單獨療效的獨立 RCT 證據目前仍較少，機轉關聯性一致，臨床證據強度稍弱。

## 臨床試驗證據

目前無相關臨床試驗登記。

> 註：文獻中提及的 TEMPO 3:4、REPRISE 等關鍵性 Phase 3 試驗雖為 Tolvaptan 在 ADPKD 的核准基礎，但本次證據包的 clinical_trials／ictrp_trials 結構化欄位查無登記資料，故依規則呈現為「無」。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT | NEJM | TEMPO 3:4：V2R 拮抗劑可抑制囊腫生長、延緩腎功能下降 |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT | NEJM | REPRISE：後期 ADPKD 患者使用 Tolvaptan 仍有腎功能保護效益 |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT（兒童） | Pediatric Nephrology | 5–17 歲兒童使用 Tolvaptan 安全性與藥效學評估（NCT02964273） |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | 系統性回顧/統合分析 | Nefrologia | 確認 Tolvaptan 治療 ADPKD 之整體療效與安全性 |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Review（共識聲明） | NDT | ERA/多囊腎病國際組織對 Tolvaptan 使用時機之共識建議 |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Cochrane 系統性回顧 | Cochrane DB Syst Rev | 評估延緩 ADPKD 疾病進展之各項介入措施 |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Review | JAMA | ADPKD 全面性回顧，涵蓋盛行率、基因型與治療現況 |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Review（EASL guideline） | J Hepatol | 囊性肝病（含多囊肝病）之診斷與管理指引 |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clin Liver Dis | ADPKD 合併多囊肝病：Tolvaptan 可延緩腎功能惡化與囊腫增長 |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annu Rev Pathol | 多囊肝病之機轉理解與治療進展回顧 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 2 項高品質 Phase 3 RCT（TEMPO 3:4、REPRISE）與多篇國際治療指引/共識聲明支持 Tolvaptan 用於 ADPKD，證據等級達 L1，且此用途已為 FDA/EMA 正式核准適應症，機轉合理性極高。
- 但香港目前無許可證、未上市，且原廠仿單警語、禁忌症、DDI 等安全性資料全數缺失（DG001 屬 Blocking 等級），在補齊監理與安全性資料前不宜貿然推進。

**若要推進需要：**
- 取得香港/原廠仿單完整警語與禁忌症資料（DG001，阻斷性缺口，需先解決才能進入 S1 安全性初評）
- 補齊正式 DrugBank 作用機轉摘要（DG002）
- 確認香港藥品進口與許可證申請途徑（目前 0 張許可證）
- 若欲單獨主張多囊肝病適應症，需補充該族群的獨立 RCT 證據

> 補充說明：本次候選清單中 rank 2–10 之預測疾病（如 renal-hepatic-pancreatic dysplasia、karyomegalic interstitial nephritis、hypertrichosis、Dandy-Walker 相關症候群等）證據等級多為 L4–L5，部分（如牙周病相關文獻）經檢視為知識圖譜/文獻檢索的實體誤配（entity mismatch），均建議 Hold，不建議進一步投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

