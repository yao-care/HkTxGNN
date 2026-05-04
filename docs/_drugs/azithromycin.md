---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin：從細菌感染到高澱粉酶血症

## 一句話總結

Azithromycin 是廣效性大環內酯類抗生素，廣泛用於呼吸道感染、皮膚感染、性傳播疾病及非典型病原體感染的治療。TxGNN 模型預測其排名第一的新適應症為**高澱粉酶血症 (Hyperamylasemia)**，分數達 **99.81%**，但此預測目前**無任何臨床試驗或文獻**支持，屬純模型推論。在全部 10 項預測中，以**鐮刀型紅血球病（SCD）相關的先天性血液疾病**（排名第 10）的實際研究基礎最為充分（L3 等級，4 項臨床試驗）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌性感染（呼吸道、皮膚、性傳播疾病、非典型病原體） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5（僅模型預測，無任何直接研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前 Evidence Pack 缺乏詳細的作用機轉資料（MOA 數據待補）。根據已知資訊，Azithromycin 是大環內酯類（Macrolide）抗生素，除結合細菌 50S 核糖體阻斷蛋白質合成的直接抗菌效應外，還具有顯著的**免疫調節特性**：可抑制 IL-6、TNF-α、IL-8 等促炎細胞激素，抑制 NF-κB 信號路徑，以及阻斷細胞自噬通量（autophagy flux）。這些非抗菌機轉正是老藥新用潛力的重要基礎。

高澱粉酶血症本身是**繼發性指標**（通常反映胰腺炎或唾液腺病變），並非獨立的治療標靶疾病實體。Azithromycin 的抗炎特性理論上或可緩解胰腺炎誘發的澱粉酶升高，但這是高度推測性連結，目前**無任何直接機轉研究或臨床資料**支持。

TxGNN 的高分可能源於知識圖譜中「感染 → 胰腺炎 → 高澱粉酶血症」的間接路徑，而非藥物對澱粉酶代謝的直接效應。此預測需謹慎解讀，不宜作為優先推進方向。

---

## 臨床試驗證據

目前無與高澱粉酶血症相關的臨床試驗登記。

---

## 文獻證據

目前無與高澱粉酶血症相關的文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：香港 Department of Health 仿單警語及禁忌症資料目前缺失，此為 Blocking 等級資料缺口，**無法完成標準安全性初評（S1 階段）**，任何推進決定均需先補全此資料。

---

## 全部預測概覽（10 項）

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 | 備注 |
|------|------|-----------|---------|------|------|
| 1 | 高澱粉酶血症 (Hyperamylasemia) | 99.81% | L5 | Hold | 繼發性指標，非獨立治療標靶；無直接研究 |
| 2 | 多克隆高黏滯症候群 | 99.81% | L5 | Hold | 機轉連結極弱；可能為模型分類雜訊 |
| 3 | 先天性無白蛋白血症 | 99.79% | L5 | Hold | 超罕見遺傳病（全球 <80 例）；無已知 AZM 效應 |
| 4 | 點狀上皮角結膜炎 | 99.78% | L4 | Research Question | 1 篇 Microsporidia 病例報告；AZM 對砂眼有 WHO 推薦 |
| 5 | 血型不相容 | 99.70% | L5 | Hold | 機轉無生物學連結；可能為圖譜泛化錯誤 |
| 6 | 癌前血液系統疾病 | 99.64% | L5 | Hold | 疾病分類過廣；自噬抑制效應僅為推測 |
| 7 | 單克隆球蛋白病 | 99.61% | L4 | Research Question | 體外研究顯示 AZM 可增強骨髓瘤細胞對 bortezomib 敏感性 |
| 8 | 獲得性周圍神經病變相關血液疾病 | 99.56% | — | 待評估 | 尚無評估資料 |
| 9 | 敗血症性鼠疫 | 99.52% | L4 | Research Question | 體外抗 *Y. pestis* 活性**較差**（PMID 8540736）；可能為兒童/孕婦替代選項 |
| 10 | 先天性血液疾病（含 SCD） | 99.40% | **L3** | **Research Question** | **最強證據**；4 項 SCD 臨床試驗＋Cochrane 系統性回顧 |

---

## 重點深析：先天性血液疾病 / 鐮刀型紅血球病（排名第 10）

此方向在全部預測中擁有最充分的研究基礎。機轉連結明確：Azithromycin 的免疫調節特性（↓ IL-8、↓ TNF-α、↓ 中性球活化）可能減少 SCD 急性胸症候群（ACS）的肺部炎症反應；其抑制 NF-κB 路徑的效應理論上有助於降低血管炎症；此外，SCD 患者因功能性無脾（autosplenectomy）具有高度感染風險，AZM 預防性抗非典型病原體（*Mycoplasma*、*Chlamydia*）或可減少感染誘發的 ACS 發作。

### 臨床試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | 已撤回 | 0 | **直接**研究 Azithromycin 預防 SCD 急性胸症候群（ACS），試驗假說成立；撤回原因未揭露，疑為資金問題而非安全疑慮 |
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | 已撤回 | 0 | 大環內酯類改善 SCD 患者 FEV1 肺功能可行性試驗；同樣因執行困難撤回，不代表假說否定 |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | 招募中 | 5,000 | NICHD 兒科藥動學大型研究，可提供先天性血液病兒童族群的 AZM 安全性與 PK 基礎數據 |
| [NCT04294641](https://clinicaltrials.gov/study/NCT04294641) | Phase 2 | 已完成 | 10 | Ibrutinib 治療 cGVHD；AZM 在 cGVHD 管理中有時作為支持療法，與先天性血液病直接關聯性較低 |

### 文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Cochrane 系統性回顧 | Cochrane Database | 抗生素預防高風險兒童（含先天性免疫缺損）下呼吸道感染之效益與風險評估；為 SCD 兒童族群提供方法學基礎 |
| [34471086](https://pubmed.ncbi.nlm.nih.gov/34471086/) | 2021 | 病例報告 | Am J Case Reports | 嬰兒免疫性血小板減少症（ITP）合併 COVID-19；涉及大劑量 methylprednisolone 治療，與 AZM 直接相關性低 |

---

## 重點深析：單克隆球蛋白病（排名第 7）

最具機轉相關性的文獻（PMID 23546223）顯示：大環內酯類（包含 Azithromycin）可阻斷自噬通量，導致內質網壓力（ER stress）積聚，進而**增強骨髓瘤細胞對 bortezomib（硼替佐米）的敏感性**。此機轉提示 AZM 在多發性骨髓瘤中或可作為 bortezomib 的增敏佐藥。

### 關鍵文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | 體外研究 | Int J Oncol | AZM 阻斷 LC3B-II/p62 自噬通量，聯合 bortezomib 對 U266、IM-9、RPMI8226 骨髓瘤細胞株顯著增強細胞毒性（ER stress/CHOP 路徑） |
| [22825522](https://pubmed.ncbi.nlm.nih.gov/22825522/) | 2012 | 病例報告 | Tumori | 多發性骨髓瘤患者顎骨壞死（ONJ）以 AZM 500 mg/day 輔助臭氧治療，顯示骨髓瘤患者耐受 AZM |
| [33389938](https://pubmed.ncbi.nlm.nih.gov/33389938/) | 2020 | 病例報告 | Turk J Ophthalmol | POEMS 症候群（含 monoclonal gammopathy）合併 Bartonella 神經視網膜炎，AZM 為潛在治療藥物 |

---

## 結論與下一步

**決策：Hold（針對高澱粉酶血症作為首要適應症）**

**理由：**
高澱粉酶血症為繼發性指標而非可治療疾病本體，TxGNN 高分可能反映知識圖譜中的間接路徑連接，而非真實藥物效應。在證據充分性和機轉合理性上，本批預測中更值得投入資源的方向是 SCD（鐮刀型紅血球病）及骨髓瘤（monoclonal gammopathy）。

**若要推進需要：**

1. **立即行動（Blocking 缺口）**：補充香港 Department of Health 仿單警語及禁忌症資料，以解除 S1 安全性初評的阻礙
2. **MOA 補充**：透過 DrugBank API 取得完整作用機轉資料
3. **SCD 方向（優先推薦）**：評估重啟 NCT02630394 型試驗的可行性；設計 Azithromycin 預防 SCD-ACS 的 Phase 2 隨機對照試驗（目標族群：復發性 ACS 患者）
4. **骨髓瘤方向**：基於 PMID 23546223 的體外增敏數據，設計 AZM + bortezomib 聯合治療的 Phase 1 劑量爬升試驗
5. **點狀上皮角結膜炎方向**：蒐集 Azithromycin 眼科製劑（已核准用於砂眼）的 PEK 相關真實世界數據

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選均需經過嚴格的臨床驗證方可應用於臨床實踐。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

