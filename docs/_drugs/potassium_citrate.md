---
layout: default
title: Potassium Citrate
parent: 高證據等級 (L1-L2)
nav_order: 605
evidence_level: L1
indication_count: 5
---

# Potassium Citrate
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Potassium Citrate（檸檬酸鉀）：老藥新用評估 — 腎結石（Nephrolithiasis）

## 一句話總結

Potassium Citrate（DrugBank DB09125）目前在香港未取得任何藥品許可證，原始核准適應症資料從缺。
TxGNN 模型對其提出多個候選新適應症，其中**腎結石 (Nephrolithiasis)** 有紮實的實證支持——
**36 個臨床試驗**與**19 篇文獻**，機轉已是確立多年的標準藥理知識，而非單純模型推測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（香港未取得許可證，無原始核准適應症紀錄） |
| 預測新適應症 | 腎結石 (Nephrolithiasis) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

DrugBank 對 Potassium Citrate 的作用機轉欄位為資料缺口，但由臨床實證累積的藥理知識已相當明確：檸檬酸鉀口服後於腎臟代謝為碳酸氫鹽，可提高尿中檸檬酸濃度並鹼化尿液。

檸檬酸與尿鈣形成可溶性複合物，抑制草酸鈣及磷酸鈣結晶的成核與聚集，同時提高的尿液 pH 有助於尿酸結石溶解。這是已確立多年的標準機轉，也是多國將檸檬酸鉀列為腎結石（尤其是低檸檬酸尿型）標準預防用藥的理由。

值得注意的是，此候選並非單純圖譜推測——多個 Phase 3/4 臨床試驗與一篇系統性回顧/統合分析已直接驗證檸檬酸鉀在結石復發預防上的效果，機轉與實證方向一致。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06003348](https://clinicaltrials.gov/study/NCT06003348) | Phase 4 | 招募中 | 25 | 測試 hydroxycitrate（檸檬酸相關分子）能否降低磷酸鈣結石復發 |
| [NCT03258190](https://clinicaltrials.gov/study/NCT03258190) | Phase 2 | 已完成 | 137 | 石灰粉療法（富含檸檬酸/檸檬酸鉀）用於高復發風險結石病人預防 |
| [NCT00004284](https://clinicaltrials.gov/study/NCT00004284) | Phase 3 | 已完成 | 300 | 緩釋磷酸鉀 vs 檸檬酸鉀，用於吸收性高鈣尿症與結石復發預防 |
| [NCT01329042](https://clinicaltrials.gov/study/NCT01329042) | Phase 4 | 已完成 | 80 | 檸檬酸氫鉀鈉用於 ESWL/PCNL 後結石復發及殘留結石之預防 |
| [NCT04021381](https://clinicaltrials.gov/study/NCT04021381) | Phase 3 | 未知 | 262 | 檸檬酸鹽用於輸尿管軟鏡術後下盞結石之無石率評估（安慰劑對照） |
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | 已撤回 | 0 | 兒童特發性高鈣尿症使用檸檬酸鉀之尿液化學與酸鹼效應（已撤回） |
| [NCT01980004](https://clinicaltrials.gov/study/NCT01980004) | Phase 2 | 已撤回 | 0 | 檸檬酸鉀補充對磷酸鈣結石高風險族群復發的效果（已撤回） |
| [NCT06966635](https://clinicaltrials.gov/study/NCT06966635) | Phase 4 | 招募中 | 312 | 檸檬酸鉀緩釋錠治療痛風合併尿路結石之探索性研究 |
| [NCT06819553](https://clinicaltrials.gov/study/NCT06819553) | Phase 2/3 | 進行中未招募 | 48 | 口服檸檬酸鉀降低輸尿管鏡術後支架結垢之效果 |
| [NCT01754779](https://clinicaltrials.gov/study/NCT01754779) | Phase 2 | 已完成 | 13 | 檸檬酸/檸檬酸鉀對磷酸鈣結石病人尿液飽和度之藥理治療效果 |

（資料庫中共有 36 個相關試驗登記，以上為最相關的 10 個。）

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27915395](https://pubmed.ncbi.nlm.nih.gov/27915395/) | 2017 | 系統性回顧/統合分析 | Urolithiasis | 檸檬酸鉀補充可有效降低碎石術前後結石復發率 |
| [40978115](https://pubmed.ncbi.nlm.nih.gov/40978115/) | 2025 | Review (Tier 1) | Clinical Kidney Journal | 檸檬酸為 TCA 循環中間產物，是尿鹼基當量及鈣結石形成之強效抑制劑，更新其生理機轉與臨床應用 |
| [40583613](https://pubmed.ncbi.nlm.nih.gov/40583613/) | 2025 | Review (Tier 1) | Arch Ital Urol Androl | 泌尿道結石治療專家共識，涵蓋檸檬酸鹽等藥物治療角色 |
| [26582172](https://pubmed.ncbi.nlm.nih.gov/26582172/) | 2016 | 回顧性研究 | Urolithiasis | 檸檬酸鉀降低低檸檬酸尿型草酸鈣結石病人的尿鈣排泄 |
| [1585829](https://pubmed.ncbi.nlm.nih.gov/1585829/) | 1992 | 原始研究 | J Bone Miner Res | 檸檬酸鉀鎂 vs 檸檬酸鉀對尿液生化與結石鹽類結晶的物理化學作用比較 |
| [39206631](https://pubmed.ncbi.nlm.nih.gov/39206631/) | 2024 | Phase II 研究 | Urologia | 益生菌+檸檬酸鉀+鎂補充可降低結石病人的尿結晶現象 |
| [33417997](https://pubmed.ncbi.nlm.nih.gov/33417997/) | 2021 | 動物實驗 | Kidney International | Chlorthalidone 併用檸檬酸鉀在遺傳性高鈣尿結石大鼠模型中減少草酸鈣結石並改善骨質 |
| [16443041](https://pubmed.ncbi.nlm.nih.gov/16443041/) | 2006 | Review (Tier 2) | Lancet | 腎結石病理生理與藥物治療總論，涵蓋檸檬酸鉀角色 |
| [3306318](https://pubmed.ncbi.nlm.nih.gov/3306318/) | 1987 | Review | Miner Electrolyte Metab | 檸檬酸鉀用於腎小管酸中毒、低檸檬酸尿性草酸鈣結石與尿酸結石之奠基性文獻 |
| [23924538](https://pubmed.ncbi.nlm.nih.gov/23924538/) | 2013 | Review | Medicina (B Aires) | 檸檬酸與腎結石：低檸檬酸尿病因與治療回顧 |

（資料庫中共有 19 篇相關文獻，以上為最相關的 10 篇。）

---

## 其他 TxGNN 預測適應症（證據不足，暫緩）

以下候選 TxGNN 分數雖高，但目前查無任何臨床試驗或文獻佐證，機轉關聯性亦屬推測，建議 **Hold**：

| 適應症 | TxGNN 分數 | 證據等級 | 決策 | 備註 |
|--------|-----------|---------|------|------|
| Familial visceral myopathy | 99.95% | L5 | Hold | 無已知機轉可連結電解質/鹼化劑與內臟肌病變 |
| Mitochondrial oxidative phosphorylation disorder (nuclear DNA) | 99.92% | L5 | Hold | 外源性檸檬酸鉀矯正粒線體呼吸鏈缺陷缺乏生理學基礎 |
| Pendred syndrome | 99.88% | L5 | Hold | 機轉方向（鹼中毒傾向）與檸檬酸鉀鹼化作用不一致 |
| Cystinosis | 99.73% | L4 | Research Question | 常合併近端腎小管酸中毒，機轉具生理合理性，但僅有 3 篇病例報告，無直接臨床試驗證據 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（香港仿單警語/禁忌資料尚未取得，列為 Blocking 資料缺口，需優先補齊才能進入安全性初評。）

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅適用於「腎結石」此一預測適應症；其餘 4 個候選維持 Hold）

**理由：**
- 檸檬酸鉀用於腎結石預防有多個 Phase 2–4 試驗及一篇系統性回顧/統合分析支持，機轉為確立多年的標準藥理知識，證據等級達 L1。
- 但該藥目前在香港**尚無任何許可證**（0 張），且缺乏 MOA 官方資料與仿單安全性資訊，須先完成法規與安全性補件才可能實際推進。

**若要推進需要：**
- 向 DrugBank／原廠取得完整作用機轉（MOA）資料
- 取得香港（或參考地區）仿單警語、禁忌症與 DDI 資料，完成 S1 安全性初評（目前為 Blocking 缺口）
- 確認香港藥品註冊路徑（目前市場狀態為未上市）
- 針對 Cystinosis（L4）候選，建議列為研究問題，規劃前驅或個案系列研究以補足實證
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

