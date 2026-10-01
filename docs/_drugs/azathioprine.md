---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 88
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine：從免疫抑制治療到 TxGNN 預測的新適應症

## 一句話總結

Azathioprine（硫唑嘌呤）是嘌呤類似物免疫抑制劑，香港已有 8 張許可證，但本次資料未提供原核准適應症文字。
TxGNN 排名第 1 的預測是**柯氏缺損性小眼畸形－肢根型發育不良症候群 (colobomatous microphthalmia-rhizomelic dysplasia syndrome)**，目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。
證據較充分的是排名第 5 和第 9 的**發炎性腸道疾病 (IBD)** 與**潰瘍性結腸炎 (UC)**，但這兩者已是臨床標準用法，不算新的老藥新用訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 柯氏缺損性小眼畸形－肢根型發育不良症候群 (colobomatous microphthalmia-rhizomelic dysplasia syndrome) |
| TxGNN 預測分數 | 99.9994%（全體排名第 37） |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

> 原適應症欄位：許可證資料中的核准適應症文字為空白，因此省略。

---

## 為什麼這個預測合理？

**這個預測在生物學上找不到合理的機轉連結。**
這是一種罕見的眼部與骨骼發育異常疾病，沒有免疫介導的病理機轉，而 azathioprine 這類嘌呤類似物免疫抑制劑正是針對免疫反應。
分數很高（0.99999）很可能反映的是知識圖譜的網路鄰近性，而非真正的生物學關聯。

目前缺乏詳細的作用機轉資料，所以無法用原機轉交叉驗證這個預測。
沒有試驗也沒有文獻，因此判定為 Hold。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 其他預測適應症總覽

排名第 1 的預測沒有證據，以下整理 TxGNN 前 10 名預測的證據狀態：

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 | 說明 |
|-----|-----------|------|---------|------|------|
| 1 | 柯氏缺損性小眼畸形－肢根型發育不良症候群 | 99.9994% | L5 | Hold | 先天發育異常，無機轉連結 |
| 2 | 短指－併指症候群 | 99.9992% | L5 | Hold | 先天肢體畸形，無合理機轉 |
| 3 | 骨關節炎易感性 | 99.7005% | L5 | Hold | 基因易感性特徵，非可治療的臨床疾病，應併入骨關節炎評估 |
| 4 | WHIM 症候群 | 99.6830% | L5 | Hold | 免疫缺陷疾病，進一步免疫抑制與骨髓抑制可能加重感染與血球低下，方向可能有害 |
| 5 | 發炎性腸道疾病 | 99.5205% | L1 | Proceed with Guardrails | 詳見下方 |
| 6 | 慢性肉芽腫症（體染色體隱性第 5 型） | 99.4096% | L5 | Hold | 吞噬細胞缺陷，免疫抑制有嚴重感染風險 |
| 7 | 骨關節炎 | 99.4002% | L4 | Hold | 僅有間接證據，無 OA 專屬療效資料 |
| 8 | 嗜中性球趨化缺陷之肉芽腫疾病 | 99.3711% | L5 | Hold | 方向可能有害 |
| 9 | 潰瘍性結腸炎 | 99.3314% | L1 | Proceed with Guardrails | 詳見下方 |
| 10 | 肢端中段發育不良（Hunter-Thompson 型） | 99.2729% | L5 | Hold | 遺傳性骨骼發育不良，無免疫成分 |

### IBD／UC 的機轉依據

Azathioprine 會轉換為 6-mercaptopurine，再轉為硫代鳥嘌呤核苷酸。
這些代謝物抑制嘌呤合成，並透過抑制 Rac1 促使 T 細胞凋亡，可合理地抑制克隆氏症與潰瘍性結腸炎的黏膜發炎。
硫嘌呤類藥物用於 IBD 已行之有年，有 Phase 3 試驗、活性對照試驗與系統性回顧支持。
由於這已是標準做法，並非新的老藥新用訊號，且本次資料未提供原核准適應症（original_indications 為空），香港仿單是否已核准 IBD 適應症需另行確認。

### IBD／UC 相關臨床試驗（節選 10 項）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | 招募中 | 300 | 新診斷中重度 UC：mirikizumab 早期治療 vs 以 azathioprine 為標準治療的對照，尚無結果 |
| [NCT05040464](https://clinicaltrials.gov/study/NCT05040464) | Phase 3 | 招募中 | 166 | 克隆氏症：與 adalimumab 併用時比較 azathioprine 與 methotrexate |
| [NCT01817972](https://clinicaltrials.gov/study/NCT01817972) | Phase 3 | 未知 | 65 | 中重度克隆氏症：Cimzia 單用 vs Cimzia 加 azathioprine，比較內視鏡分數改善 |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | 完成 | 78 | 克隆氏症術後內視鏡復發：azathioprine vs mesalazine 預防臨床復發 |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | 完成 | 83 | 克隆氏症術後復發預防：azathioprine 對比 mesalazine 的優越性 |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | 提前終止 | 242 | 中重度 UC：infliximab 單用或加 azathioprine vs azathioprine 單用 |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | 未知 | 84 | UC：低劑量 azathioprine 加 allopurinol vs azathioprine 單用 |
| [NCT00796250](https://clinicaltrials.gov/study/NCT00796250) | Phase 3 | 提前終止 | 9 | 類固醇依賴克隆氏症：infliximab 作為銜接治療，僅收 9 人，檢定力不足 |
| [NCT00167882](https://clinicaltrials.gov/study/NCT00167882) | Phase 4 | 完成 | 24 | 5-ASA 對 azathioprine／6-MP 代謝物濃度的影響，支持交互作用的安全防護 |
| [NCT00521950](https://clinicaltrials.gov/study/NCT00521950) | N/A | 完成 | 853 | 硫嘌呤使用前 TPMT 基因型檢測的成本效益（荷蘭前瞻性隨機試驗） |

### IBD／UC 相關文獻（節選 10 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | 急性重度 UC 對靜脈類固醇有反應者：infliximab 加 azathioprine vs azathioprine 單用（ACTIVE 試驗） |
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | 系統性回顧 | Cochrane Database Syst Rev | Azathioprine 與 6-MP 用於 UC 維持緩解（更新版） |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | 系統性回顧 | Cochrane Database Syst Rev | 同上主題的前一版回顧 |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | 統合分析 | Aliment Pharmacol Ther | Azathioprine 與 mercaptopurine 在 UC 的療效 |
| [27450969](https://pubmed.ncbi.nlm.nih.gov/27450969/) | 2016 | 統合分析 | J Dig Dis | 低劑量 azathioprine 用於慢性活動性 UC 的療效與安全性 |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | 回顧 | J Crohns Colitis | 硫嘌呤治療 IBD 的最新發現與展望 |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | 回顧 | World J Gastroenterol | 6-TGN 濃度與療效相關，高 6-MMP 濃度與肝毒性、骨髓毒性相關 |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | 藥物基因體學回顧 | J Gastroenterol Hepatol | 代謝物個體差異大，重度毒性導致 9-25% 病人停藥 |
| [24117596](https://pubmed.ncbi.nlm.nih.gov/24117596/) | 2013 | 觀察性研究、系統性回顧與統合分析 | Aliment Pharmacol Ther | 對 azathioprine 不耐受者改用 mercaptopurine 的安全性 |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | 機轉／轉譯研究 | Cell Rep Med | 腸道共生菌降低 6-MP 生物可用性，促成 azathioprine 治療失敗 |

---

## 香港上市資訊

香港共 8 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症文字，故不列這兩欄。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-03804 | IMURAN TAB 50MG | ASPEN PHARMACARE ASIA LIMITED |
| HK-30975 | IMURAN TAB 25MG | ASPEN PHARMACARE ASIA LIMITED |
| HK-44747 | AZAMUN TAB 50MG | UNITED ITALIAN CORP (HK) LTD |
| HK-65195 | AZAMUN TABLETS 25MG | UNITED ITALIAN CORP (HK) LTD |
| HK-55083 | APO-AZATHIOPRINE TAB 50MG | HIND WING CO LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（針對排名第 1 的預測）

**理由：**
- 排名第 1 的疾病是先天性發育異常，沒有免疫機轉可讓 azathioprine 發揮作用，也沒有任何試驗或文獻，高分很可能只是知識圖譜的拓撲假象。
- 排名前 10 名中，只有 IBD 與 UC 有實質證據（L1，建議 Proceed with Guardrails）。這屬於既有標準用法的確認，不是新適應症的發現。
- WHIM 症候群與兩種肉芽腫疾病的作用方向可能有害，不建議推進。

**若要推進需要：**
- 確認 IBD／UC 是否已列入香港許可證的核准適應症。本次許可證的適應症文字皆為空白，需取得香港衛生署的仿單。
- 取得作用機轉與安全性資料（警語、禁忌症）。目前這兩項都缺，安全性篩檢無法進行。
- 用於 IBD／UC 時，需配合以下防護：
  - 使用前做 TPMT／NUDT15 基因型或活性檢測。
  - 監測血球計數（CBC）與肝功能。
  - 提醒淋巴瘤與皮膚癌風險。
  - 注意 5-ASA 併用會提高硫嘌呤代謝物濃度（NCT00167882），並謹慎用於懷孕族群。
- 若仍想探索排名第 1 的預測，需先有機轉層面的前臨床假說，否則不建議投入資源。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

