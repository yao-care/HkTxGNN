---
layout: default
title: Oteracil
parent: 高證據等級 (L1-L2)
nav_order: 648
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-28
description: "Oteracil：預測新適應症為大腸腫瘤 (Colonic Neoplasm)（證據等級 L1）。原適應症：胃癌（gastric cancer）"
monitor_inn: "Oteracil"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "rectosigmoid junction neoplasm", "benign neoplasm of cecum", "colonic lymphangioma", "colon leiomyoma", "cavernous hemangioma of colon"]
---

# Oteracil
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

## Oteracil：從胃癌到大腸腫瘤
{: .text-alpha }

## 一句話總結

Oteracil 是 S-1 複方（tegafur + gimeracil + oteracil）的成分之一，原本用於胃癌治療。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效，
目前有 **6 個臨床試驗**和 **10 篇文獻**支持這個方向。需注意，抗腫瘤療效主要來自複方中的 5-FU 前驅藥 tegafur，並非 oteracil 單獨作用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌（gastric cancer） |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L1 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。不過，根據已知資訊，Oteracil 是 S-1 複方的一部分。它在腸胃道抑制乳清酸磷酸核糖轉移酶，減少 5-FU 在局部的活化，從而降低腸胃道毒性。複方中的 tegafur 是 5-FU 前驅藥，gimeracil 則抑制 DPD 酶以維持 5-FU 的血中濃度。

大腸癌的抗腫瘤效果來自 5-FU 成分。因此現有證據支持的是 **S-1 作為複方療法**，而不是 oteracil 作為單獨藥物。

胃癌與大腸癌同屬消化道上皮腺癌，對氟嘧啶類藥物（fluoropyrimidine）都有反應，因此這項延伸在生物學上合理。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 完成 | 1535 | UFT+Leucovorin vs. S-1 用於 Stage III 結腸癌術後輔助治療，為 S-1 用於結腸癌的大型直接證據 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 狀態未知 | 1191 | SOX（奧沙利鉑+S-1）vs. XELOX 用於 Stage III 大腸直腸癌輔助化療；結果尚未經證實 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 狀態未知 | 40 | S-1 + Bevacizumab 用於先前化療失敗的不可切除或復發大腸直腸癌 |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | 狀態未知 | 82 | Raltitrexed + S-1 用於標準化療失敗的轉移性大腸直腸癌，主要終點為無惡化存活期 |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | 尚未招募 | 52 | Fruquintinib + S-1 複方用於晚期轉移性大腸直腸癌三線治療，單臂試驗，尚無結果 |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | 提前終止 | 20 | S-1 或 Capecitabine 併用奧沙利鉑對冠狀動脈血流的影響，主要提供心臟毒性的安全性資訊，而非療效 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | 回溯性世代研究 | Gan To Kagaku Ryoho | 87 位晚期或復發結腸癌患者接受 S-1 + irinotecan，分析 3–4 級血液毒性（16.1%）的風險因子 |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | 前臨床（異種移植） | Oncol Rep | Irinotecan 可透過下調腫瘤內胸苷酸合成酶，克服結腸癌異種移植對 5-FU 的抗藥性，與 S-1 併用可增強抗腫瘤活性 |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | 病例報告＋文獻回顧 | J Oncol Pharm Pract | S-1 治療後出現以三酸甘油酯升高為主的高三酸甘油酯血症 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | 病例報告 | Eur J Dermatol | TS-1 引起紅皮症、廣泛黏膜受損與手足症候群 |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | 病例報告 | Gan To Kagaku Ryoho | 結腸癌患者使用 S-1 複方後改用 CAPOX+BEV，出現奧沙利鉑誘發的急性周邊神經病變合併尿滯留 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | 病例報告 | Anticancer Res | S-1 併用 CPT-11 使結腸癌肝轉移達到完全緩解並維持 |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | 病例報告 | Gan To Kagaku Ryoho | SOX 併用 panitumumab 降階治療後，成功對無法切除的大腸癌肝轉移進行兩階段肝切除 |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | 病例報告 | Gan To Kagaku Ryoho | 大腸癌術後腹膜復發，經腹腔鏡反覆切除 |
| [30692384](https://pubmed.ncbi.nlm.nih.gov/30692384/) | 2018 | 病例報告 | Gan To Kagaku Ryoho | 結腸癌術後復發的疼痛，以電腦斷層導引腹腔神經叢神經鬆解獲得完全緩解 |

以上文獻多為病例報告與前臨床研究，並無隨機對照試驗，療效結論的主要依據仍是前述臨床試驗。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67976 | TEGO CAPSULES 20MG/5.8MG/19.6MG | — | — |
| HK-67977 | TEGO CAPSULES 25MG/7.25MG/24.5MG | — | — |
| HK-61181 | TS-ONE 25 CAP | — | — |
| HK-61182 | TS-ONE 20 CAP | — | — |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（氟嘧啶類 Fluoropyrimidine 複方，tegafur 為 5-FU 前驅藥） |
| 骨髓抑制風險 | 中度（文獻中 S-1 + irinotecan 治療的 3–4 級血液毒性發生率為 16.1%） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝腎功能、電解質；另可留意血脂（三酸甘油酯）、皮膚與黏膜反應、手足症候群 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

骨髓抑制數據與不良反應（高三酸甘油酯血症、紅皮症、手足症候群）來自上述文獻；致吐性分級為依藥物類別所作的判斷。詳細內容請參考原廠仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。

另外，文獻與試驗顯示 S-1 相關的已知風險包括手足症候群、嚴重皮膚與黏膜反應、高三酸甘油酯血症及血液毒性。有一項試驗（NCT02216149）曾探討氟嘧啶類藥物的潛在心臟毒性。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 2 項 Phase 3 RCT 直接測試 S-1 用於大腸癌，其中 NCT00660894 已完成且規模大（n=1535），另有多項 Phase 2 試驗，證據等級為 L1。
- 但療效來自 S-1 複方（主要是 5-FU 成分），並非 oteracil 單獨作用；NCT03448549 的狀態為未知，結果也尚待確認，因此需設置防護條件。

**若要推進需要：**
- 取得並確認 NCT00660894 與 NCT03448549 的正式結果與療效數據
- 補充 Oteracil 詳細作用機轉（MOA）資料
- 取得香港衛生署仿單的警語與禁忌症，以及核准適應症文字（目前許可證資料中該欄位為空白）
- 確認推進對象為 S-1 複方療法，而非 oteracil 單方
- 擬定血液學、皮膚黏膜與血脂等的安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

