---
layout: default
title: Bleomycin
parent: 高證據等級 (L1-L2)
nav_order: 125
evidence_level: L1
indication_count: 6
---

# Bleomycin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **6** 個
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

# Bleomycin：從淋巴瘤到網狀細胞肉瘤（Reticulum Cell Sarcoma）

## 一句話總結

Bleomycin（博來黴素）是一種細胞毒性抗腫瘤藥物，原本用於何杰金氏淋巴瘤、非何杰金氏淋巴瘤及頭頸癌等治療。
TxGNN 模型預測的首要候選為**腦脊髓馬尾腫瘤**，但該項僅有 1 篇文獻、屬於純模型預測。本報告以證據最完整的**網狀細胞肉瘤 (Reticulum Cell Sarcoma)** 為主要評估對象，目前有 **11 個臨床試驗**和 **20 篇文獻**支持。網狀細胞肉瘤是已淘汰的舊名詞，大致對應現今的瀰漫性大 B 細胞淋巴瘤或其他非何杰金氏淋巴瘤，因此較接近既有適應症的重新歸類，而非全新的再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 何杰金氏淋巴瘤、非何杰金氏淋巴瘤、頭頸癌等（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 網狀細胞肉瘤 (Reticulum Cell Sarcoma) |
| TxGNN 預測分數 | 99.14% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

> 註：TxGNN 預測排名第 1 的是腦脊髓馬尾腫瘤（99.30%，L5，僅模型預測，建議 Hold）。排名第 3 的網狀細胞肉瘤證據最充分，故以此為重點。其他候選的簡要比較見「其他預測適應症」。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Bleomycin 是一種使 DNA 股斷裂的細胞毒性藥物，在何杰金氏淋巴瘤（如 ABVD 療法）及多種非何杰金氏淋巴瘤的化療組合（如 MACOP-B、ProMACE-CytaBOM）中已有長期使用經驗，機轉上可能適用於網狀細胞肉瘤。

網狀細胞肉瘤是舊式分類名稱，現今多歸入瀰漫性大 B 細胞淋巴瘤或其他非何杰金氏淋巴瘤，與 Bleomycin 已知的淋巴瘤適應症高度重疊。1971–1972 年的早期研究已描述 Bleomycin 單藥用於網狀細胞肉瘤（22 例）及蕈樣肉芽腫的反應。

因此這個預測更像是疾病名稱的重新對應。真正需要把關的是安全性，尤其是肺毒性與 HIV 相關淋巴瘤的免疫抑制問題。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00002565](https://clinicaltrials.gov/study/NCT00002565) | Phase 3 | 完成 | 61 | 交替三藥療法 vs CHOP 用於中高度惡性淋巴瘤，樣本數小 |
| [NCT00002835](https://clinicaltrials.gov/study/NCT00002835) | Phase 3 | 完成 | 116 | 早期強化 vs 交替三藥療法用於預後不良淋巴瘤 |
| [NCT00005867](https://clinicaltrials.gov/study/NCT00005867) | Phase 3 | 完成 | 310 | CHOP vs PMitCEBO 用於低風險侵襲性非何杰金氏淋巴瘤 |
| [NCT00003815](https://clinicaltrials.gov/study/NCT00003815) | Phase 3 | 未知 | 未提供 | 高劑量化放療加自體骨髓移植，Bleomycin 的角色不明確 |
| [NCT00003110](https://clinicaltrials.gov/study/NCT00003110) | Phase 2 | 完成 | 5 | 72 小時連續輸注 Bleomycin 作為 AIDS 相關及一般非何杰金氏淋巴瘤的救援治療，人數極少 |
| [NCT00002571](https://clinicaltrials.gov/study/NCT00002571) | Phase 2 | 完成 | 52 | ProMACE-CytaBOM 合併抗病毒治療用於 AIDS 相關淋巴瘤 |
| [NCT00002657](https://clinicaltrials.gov/study/NCT00002657) | Phase 2 | 完成 | 20 | 調整免疫抑制、干擾素與 ProMACE-CytaBOM 用於心臟移植後淋巴增生 |
| [NCT00002524](https://clinicaltrials.gov/study/NCT00002524) | Phase 2 | 完成 | 46 | AIDS 相關淋巴瘤組合化療先導研究 |
| [NCT00032149](https://clinicaltrials.gov/study/NCT00032149) | Phase 1/2 | 未知 | 30 | PMitCEBO 加 G-CSF 用於預後良好的 HIV 相關淋巴瘤 |
| [NCT00031902](https://clinicaltrials.gov/study/NCT00031902) | Phase 1 | 未知 | 未提供 | Rituximab 加 PVB 化療用於 HIV 相關非何杰金氏淋巴瘤 |

另有 NCT00689845（原發性縱膈 B 細胞淋巴瘤臨床病理研究，觀察性）及 NCT00983944（Phase 2，已撤回，0 人）與本評估關聯較低，未列入表中。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [4109401](https://pubmed.ncbi.nlm.nih.gov/4109401/) | 1972 | 臨床研究 | British Medical Journal | Bleomycin 單藥治療後期何杰金氏病、淋巴肉瘤、網狀細胞肉瘤（22 例）及蕈樣肉芽腫；何杰金氏病患者緩解率約 29% |
| [4107632](https://pubmed.ncbi.nlm.nih.gov/4107632/) | 1971 | 臨床研究 | Archives of Dermatology | Bleomycin 用於蕈樣肉芽腫與網狀細胞淋巴瘤 |
| [14962711](https://pubmed.ncbi.nlm.nih.gov/14962711/) | 2004 | 隨機試驗長期分析 | European Journal of Cancer | 三項 EORTC 試驗共 936 位侵襲性非何杰金氏淋巴瘤患者，評估含 Bleomycin 的 CHVmP/BV 療法長期療效 |
| [40030008](https://pubmed.ncbi.nlm.nih.gov/40030008/) | 2025 | 隨機試驗事後分析 | Blood Advances | GAINED 試驗中原發性縱膈 B 細胞淋巴瘤的中期 PET 可預測預後（ACVBP 可含 Bleomycin） |
| [24014242](https://pubmed.ncbi.nlm.nih.gov/24014242/) | 2013 | 合併分析 | Blood | 19 項前瞻試驗共 1546 位 HIV 相關非何杰金氏淋巴瘤患者的治療因素分析 |
| [27888880](https://pubmed.ncbi.nlm.nih.gov/27888880/) | 2016 | 回顧 | Hematology/Oncology Clinics of North America | 原發性縱膈 B 細胞淋巴瘤治療優化，強調首選有效化學免疫療法 |
| [15934513](https://pubmed.ncbi.nlm.nih.gov/15934513/) | 2005 | 回顧 | Oncology (Williston Park) | 法國 GELA 對侵襲性非何杰金氏淋巴瘤的治療觀點 |
| [15202521](https://pubmed.ncbi.nlm.nih.gov/15202521/) | 2003 | 回顧 | Leukemia & Lymphoma | 原發性縱膈 B 細胞淋巴瘤病理生物學；MACOP-B 加放療可能是較佳誘導策略 |
| [11785838](https://pubmed.ncbi.nlm.nih.gov/11785838/) | 2002 | 文獻 | Recent Results in Cancer Research | HIV 相關非何杰金氏淋巴瘤的預後因子，涉及 m-BACOD 方案 |
| [6187214](https://pubmed.ncbi.nlm.nih.gov/6187214/) | 1983 | 病例報告 | American Journal of Medicine | 淋巴瘤患者發生 Bleomycin 相關致命性高熱 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51279 | BLEOCIN FOR INJ 15MG (VIALS)（廠商：MAIN LIFE CORP LTD） | 注射劑（粉末，瓶裝） | 資料中未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（糖肽類抗腫瘤抗生素，造成 DNA 股斷裂） |
| 骨髓抑制風險 | 相對較低（早期文獻提到具保護骨髓的特性，可給予較高累積劑量） |
| 致吐性分級 | 低 |
| 監測項目 | 肺功能與胸部影像（累積劑量、年齡為肺毒性風險因子）、CBC、肝腎功能；首次用藥前後留意發熱反應 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

其餘細節請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **肺毒性**：文獻顯示 Bleomycin 肺毒性與年齡及累積劑量相關，並可能增加放射性肺炎風險，對肺部淋巴瘤或需縱膈放療的患者尤須注意。
- **急性高熱反應**：曾有致命性高熱病例報告，通常出現在初次注射後，建議先給予試驗劑量。
- **HIV 相關淋巴瘤**：需考量免疫抑制與藥物交互作用。
- **藥物交互作用**：資料庫共記錄 100 筆。多數嚴重度未分級，僅 Levofloxacin 為輕微。部分列出的藥物包括 Pantoprazole、Palonosetron、Aprepitant、Morphine、Omeprazole、Vancomycin、Prednisone、Clarithromycin 等。
- 完整的警語與禁忌症請參考原廠仿單。

---

## 其他預測適應症（簡要比較）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|-----------|-----------|---------|------|------|
| 腦脊髓馬尾腫瘤 | 99.30% | L5 | Hold | 僅 1 篇不直接相關文獻；Bleomycin 穿透中樞神經系統能力差 |
| 成人星狀細胞腫瘤 | 99.28% | L3 | Research Question | 僅有早期小型研究（含腫瘤內輸注 Phase I），無隨機試驗確認；全身使用受血腦屏障與肺毒性限制，需局部給藥 |
| 原發性肺淋巴瘤 | 99.10% | L4 | Research Question | 無登記試驗，證據間接；肺毒性是重要顧慮 |
| 肺母細胞瘤 | 99.04% | L4 | Hold | 僅 2 篇病例報告 |
| 肺高分化胎兒型腺癌 | 99.03% | L5 | Hold | 無試驗與文獻 |

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對網狀細胞肉瘤／侵襲性非何杰金氏淋巴瘤）

**理由：**
- 有 3 項已完成的 Phase 3 隨機試驗及多項 Phase 2 試驗涉及含 Bleomycin 或相關方案的侵襲性淋巴瘤，且此適應症與既有淋巴瘤用途高度重疊。但這些試驗人數偏小，多數比較的是整體化療組合，Bleomycin 單獨貢獻難以釐清。
- 其他預測適應症（尤其腦脊髓馬尾腫瘤、肺部腫瘤）證據薄弱，建議暫緩。

**若要推進需要：**
- 取得香港許可證的核准適應症與仿單警語、禁忌症（目前缺乏）
- 補充 Bleomycin 的作用機轉資料
- 確認「網狀細胞肉瘤」在現行分類下對應的具體淋巴瘤亞型，並確認各亞型是否已在核准適應症內
- 制定肺毒性監測計畫（肺功能、累積劑量、年齡）
- 針對 HIV 相關淋巴瘤族群，評估免疫抑制與藥物交互作用管理
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

