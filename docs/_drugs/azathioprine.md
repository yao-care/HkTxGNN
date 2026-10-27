---
layout: default
title: Azathioprine
parent: 高證據等級 (L1-L2)
nav_order: 90
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Azathioprine：預測新適應症為發炎性腸道疾病 (Inflammatory Bowel Disease)（證據等級 L1）。原適應症：類風濕性關節炎"
monitor_inn: "AZATHIOPRINE"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "osteoarthritis susceptibility", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Azathioprine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

## Azathioprine：從類風濕性關節炎到發炎性腸道疾病
{: .text-alpha }

## 一句話總結

Azathioprine（硫唑嘌呤）是一種嘌呤類抗代謝免疫抑制劑，原本用於類風濕性關節炎。
TxGNN 模型的最高分預測（骨骼或眼部罕見發育症候群）缺乏任何證據支持，因此本報告以證據最充分的預測 **發炎性腸道疾病 (Inflammatory Bowel Disease, IBD)** 為重點，目前有 **23 個臨床試驗**和 **19 篇文獻**支持這個方向。需注意，azathioprine 用於 IBD 已是臨床常規，更接近「已確立的用法」而非全新再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎（香港許可證未登載適應症文字） |
| 預測新適應症 | 發炎性腸道疾病 (Inflammatory Bowel Disease) |
| TxGNN 預測分數 | 99.52% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Proceed with Guardrails |

> 補充：TxGNN 排名前兩名（分數 99.999%）為「眼缺損小眼畸形—肢根型發育不良症候群」與「短指併指症候群」，兩者皆無臨床試驗與文獻，機轉上也無合理關聯，建議 Hold。排名第 9 的潰瘍性結腸炎 (Ulcerative Colitis，分數 99.33%) 亦有充分證據，與 IBD 屬同一方向。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。根據已知資訊，azathioprine 在體內轉化為 6-mercaptopurine 及硫鳥嘌呤核苷酸，抑制嘌呤合成與 Rac1 介導的 T 細胞存活訊號，產生免疫抑制作用。

類風濕性關節炎與 IBD 都是免疫介導的慢性發炎疾病，T 細胞過度活化是共同的病理特徵。因此，能抑制淋巴球增殖、誘導 T 細胞凋亡的 azathioprine，在機轉上適用於 IBD 的緩解維持與減少類固醇用量。文獻中也指出，azathioprine 與 6-MP 是 IBD 的一線免疫調節劑，並常與抗 TNF 藥物併用。

---

## 臨床試驗證據

資料中共有 23 個與 IBD 相關的試驗，以下列出最相關的 10 個（優先列出與 azathioprine 直接相關者）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | 提前終止 | 242 | Infliximab 單用、合併 azathioprine 與 azathioprine 單用於中重度潰瘍性結腸炎之比較 |
| [NCT00984568](https://clinicaltrials.gov/study/NCT00984568) | Phase 3 | 提前終止 | 28 | 傳統階梯式療法（含 azathioprine）vs. infliximab，樣本數很小 |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | 完成 | 83 | Azathioprine vs. mesalazine 預防克隆氏症術後復發 |
| [NCT00098111](https://clinicaltrials.gov/study/NCT00098111) | Phase 3 | 提前終止 | 31 | Imuran 於活動性克隆氏症的劑量範圍研究 |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Phase 3 | 未知 | 84 | 低劑量 azathioprine 加 allopurinol vs. azathioprine 單用於潰瘍性結腸炎 |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Phase 4 | 完成 | 211 | Infliximab 合併抗代謝藥 vs. 單用，於克隆氏症持續緩解患者 |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Phase 4 | 完成 | 65 | 急性重度結腸炎：早期 azathioprine 加 infliximab vs. 類固醇加 azathioprine |
| [NCT02247258](https://clinicaltrials.gov/study/NCT02247258) | Phase 2 | 提前終止 | 63 | 迴腸型克隆氏症術後：系統性 vs. 內視鏡導向的 azathioprine 治療 |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | 招募中 | 300 | Mirikizumab 先行療法 vs. azathioprine 標準療法於新診斷潰瘍性結腸炎 |
| [NCT03393247](https://clinicaltrials.gov/study/NCT03393247) | 未分期 | 未知 | 160 | Azathioprine 與 infliximab 同時或延後 14 週合併於克隆氏症 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE 試驗：急性重度潰瘍性結腸炎，infliximab 加 azathioprine vs. azathioprine 單用 |
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | Azathioprine/6-MP 維持潰瘍性結腸炎緩解之更新回顧 |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 同上主題之 2016 版回顧 |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | 統合分析 | Aliment Pharmacol Ther | Azathioprine 與 mercaptopurine 於潰瘍性結腸炎的療效 |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Review | J Gastroenterol Hepatol | 硫嘌呤藥物遺傳學與代謝物監測 |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Azathioprine 在 IBD 的分子機轉與臨床意涵 |
| [15177535](https://pubmed.ncbi.nlm.nih.gov/15177535/) | 2004 | Review | Gastroenterol Clin North Am | Azathioprine 與 6-MP 治療 IBD 的療效與毒性 |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohns Colitis | 硫嘌呤於 IBD 的新發現與展望 |
| [30889246](https://pubmed.ncbi.nlm.nih.gov/30889246/) | 2019 | 前臨床/機轉研究 | Inflamm Bowel Dis | Azathioprine 經 mTORC1 與 PERK 誘導自噬 |
| [34287682](https://pubmed.ncbi.nlm.nih.gov/34287682/) | 2021 | Review | J Gastroenterol | 硫嘌呤藥物基因體學與 IBD 妊娠 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-03804 | IMURAN TAB 50MG | 錠劑 | 資料未登載 |
| HK-30975 | IMURAN TAB 25MG | 錠劑 | 資料未登載 |
| HK-44747 | AZAMUN TAB 50MG | 錠劑 | 資料未登載 |
| HK-65195 | AZAMUN TABLETS 25MG | 錠劑 | 資料未登載 |
| HK-55083 | APO-AZATHIOPRINE TAB 50MG | 錠劑 | 資料未登載 |

共 8 張有效單方許可證，上表僅列 5 張主要許可證。

---

## 細胞毒性

Azathioprine 並非傳統抗腫瘤藥物，但屬嘌呤類抗代謝藥，具骨髓抑制特性。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗代謝類免疫抑制劑（硫嘌呤類） |
| 骨髓抑制風險 | 中至高（文獻指出與 6-MMP 高濃度及 TPMT/NUDT15 變異相關） |
| 監測項目 | CBC（含分類）、肝功能、TPMT/NUDT15 基因型、6-TGN/6-MMP 代謝物 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜標示的疾病禁忌（非仿單原文）**：胰臟炎、血小板減少、貧血（含巨球性貧血）、腎功能不全、感染性疾病（含真菌感染、皮癬菌感染）、淋巴瘤（含原發性中樞神經淋巴瘤、淋巴肉瘤、肝脾 T 細胞淋巴瘤）、肝靜脈血栓與 Budd-Chiari 症候群。
- **藥物交互作用**（共查得 100 筆，以下為主要者）：
  - 中度：mesalazine、balsalazide、olsalazine、sulfasalazine（5-ASA 類）
  - 輕度：硫酸鋅、醋酸鋅、葡萄糖酸鋅
  - 另有 allopurinol 併用需謹慎降低劑量（來自試驗與推論資料，非交互作用資料庫所列）
- **文獻提及的重點風險**：骨髓毒性、肝毒性、胰臟炎、淋巴瘤與皮膚癌風險、感染風險。

香港仿單的警語與禁忌資料目前缺漏，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅限 IBD / 潰瘍性結腸炎方向）

**理由：**
- 有多個 Phase 3 試驗、Cochrane 系統性回顧及 2025 年 RCT 支持 azathioprine 用於 IBD。但多數 Phase 3 試驗已提前終止，或 azathioprine 僅為對照或併用組，直接證據強度有限。
- 此用途已是臨床常規，不屬新穎再利用。其餘高分預測（罕見發育症候群、WHIM 症候群、慢性肉芽腫病、骨關節炎等）無證據或有安全疑慮，建議 Hold。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症
- 確認香港許可證是否已涵蓋 IBD 適應症
- 建立 TPMT/NUDT15 基因檢測與 CBC、肝功能監測計畫
- 補充作用機轉資料（DrugBank）
- 評估併用 allopurinol、5-ASA 類與抗 TNF 藥物時的用藥管理
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

