---
layout: default
title: Oteracil
parent: 僅模型預測 (L5)
nav_order: 635
evidence_level: L5
indication_count: 10
---

# Oteracil
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

# Oteracil：從 S-1 複方輔助成分到大腸腫瘤

## 一句話總結

Oteracil（氧嗪酸鉀）是 S-1 複方（tegafur／gimeracil／oteracil）的成分之一，作用是降低腸胃道毒性，本身不是抗腫瘤藥。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效，目前有 **8 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過這些證據支持的是 **S-1 複方整體**，不能推論到 oteracil 單方。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（僅限 S-1 複方；oteracil 單方無直接證據） |
| 香港上市 | ✓ 已上市（含 oteracil 的複方製劑） |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Oteracil 是 S-1 的成分之一。它在腸胃道黏膜抑制乳清酸磷酸核糖轉移酶（OPRT），減少 5-FU 在腸道局部的活化，因此能降低腸胃道毒性。動物藥動學研究（PMID 10997934）也顯示，口服 S-1 後 oteracil 主要分布在小腸細胞內。

大腸腫瘤是 S-1 複方已有多項研究的適應症。多個 Phase 3 試驗（ACTS-CC、ACTS-RC 等）在大腸與直腸癌中驗證了 S-1 的療效，S-1 在亞洲部分地區也已是大腸直腸癌的既有用藥。所以這個預測更接近「確認既有用途」，不是真正的老藥新用。

**使用上的限制：** 療效只能歸因於固定組合的 S-1 複方，不應外推到 oteracil 單方。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | 完成 | 161 | S-1 vs Capecitabine 用於轉移性大腸直腸癌第一線治療（SALTO），比較口服氟嘧啶類藥物的安全性 |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 完成 | 1535 | UFT+Leucovorin vs TS-1 用於 Stage III 結腸癌輔助治療，並探討基因表現預測因子 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 未知 | 1191 | SOX (S-1+Oxaliplatin) vs XELOX 用於 Stage III 大腸直腸癌輔助化療 |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | 未知 | 42 | S-1＋口服 Leucovorin＋Oxaliplatin (SOL) 用於未治療的轉移性大腸直腸癌，支持可行性 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 未知 | 40 | S-1＋Bevacizumab 用於先前化療失敗的無法切除或復發大腸直腸癌 |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | 未知 | 82 | Raltitrexed＋S-1 用於標準化療失敗的轉移性大腸直腸癌，主要終點為無惡化存活期 |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | 尚未招募 | 52 | Fruquintinib＋S-1 用於晚期轉移性大腸直腸癌第三線治療（單臂），尚無結果 |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | 提前終止 | 20 | S-1 與 Capecitabine 併用 Oxaliplatin 對冠狀動脈血流的影響，屬安全性終點，非療效 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24942277](https://pubmed.ncbi.nlm.nih.gov/24942277/) | 2014 | RCT (Phase 3) | Ann Oncol | ACTS-CC：評估 S-1 作為 Stage III 結腸癌輔助化療，對比 UFT/LV 的非劣性 |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT (Phase 3) | Ann Oncol | ACTS-RC：S-1 vs UFT 用於 Stage II/III 直腸癌輔助化療 |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT (Phase 3) | Clin Colorectal Cancer | ACTS-CC 02：SOX vs UFT/LV 用於高風險 Stage III 結腸癌的優越性試驗 |
| [26036466](https://pubmed.ncbi.nlm.nih.gov/26036466/) | 2015 | RCT (Phase 2) | BMC Cancer | 比較 S-1 用於術後大腸直腸癌的給藥時程，以改善治療完成率 |
| [22415232](https://pubmed.ncbi.nlm.nih.gov/22415232/) | 2012 | RCT 安全性分析 | Br J Cancer | ACTS-CC 計畫中的安全性分析，比較 UFT/LV 與 S-1 |
| [41724114](https://pubmed.ncbi.nlm.nih.gov/41724114/) | 2026 | 世代研究 | Eur J Cancer | 真實世界研究：因 Capecitabine 毒性中斷的結腸癌病人，改用 S-1 輔助治療的安全性與可行性 |
| [32189156](https://pubmed.ncbi.nlm.nih.gov/32189156/) | 2020 | 臨床研究 | Int J Clin Oncol | KSCC1303：S-1＋Oxaliplatin 用於 Stage III 結腸癌的 3 年無病存活期最終分析 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | 共識指引 | Clin Colorectal Cancer | 亞洲轉移性大腸直腸癌治療指引共識 |
| [10897209](https://pubmed.ncbi.nlm.nih.gov/10897209/) | 2000 | Review | Gan To Kagaku Ryoho | 說明 S-1 的設計概念：增強 5-FU 療效並降低腸胃道毒性 |
| [20500514](https://pubmed.ncbi.nlm.nih.gov/20500514/) | 2010 | 前臨床 | Cancer Sci | 以新型淋巴結轉移模型比較 S-1 與 UFT/LV 的抗轉移效果 |

## 香港上市資訊

資料庫中的劑型與核准適應症欄位皆為空白，以下僅列出可確認的資訊。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67976 | TEGO CAPSULES 20MG/5.8MG/19.6MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-67977 | TEGO CAPSULES 25MG/7.25MG/24.5MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-61181 | TS-ONE 25 CAP | DKSH HONG KONG LIMITED |
| HK-61182 | TS-ONE 20 CAP | DKSH HONG KONG LIMITED |

## 細胞毒性

Oteracil 本身不具抗腫瘤活性，但它所屬的 S-1 複方含氟嘧啶類（fluoropyrimidine）細胞毒性成分，因此列出此章節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（S-1 複方為氟嘧啶類口服製劑，oteracil 為腸胃道毒性保護成分） |
| 其他項目 | 骨髓抑制風險、致吐性、監測項目與處置防護，請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：資料庫未查到 oteracil 的交互作用紀錄。
- **文獻中的不良反應訊號（S-1 複方）**：
  - 手足症候群、紅皮症合併廣泛黏膜受損（PMID 28414195，個案報告）。
  - 高三酸甘油脂血症（PMID 32936722，個案報告）。
  - 以 Capecitabine 為對照時，S-1 的手足症候群與心血管毒性發生率較低（PMID 41724114 背景描述）。

香港衛生署仿單的警語與禁忌症尚未取得，其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 2 個已完成的 Phase 3 RCT（NCT00660894、NCT01918852），另有多項 ACTS 系列 RCT 支持 S-1 用於大腸直腸癌，證據等級可達 L1。但證據對象是 S-1 固定複方，oteracil 單方沒有任何抗腫瘤證據。
- TxGNN 的其他 9 個預測多為良性病灶（如絨毛狀腺瘤、脂肪瘤、血管瘤、平滑肌瘤）或無臨床證據的項目，多屬圖譜鄰近性造成的假訊號，建議 Hold。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症（目前是阻斷性資料缺口）。
- 補充 oteracil 的作用機轉資料（DrugBank 查詢）。
- 確認香港 4 張許可證（TEGO、TS-ONE）是否已核准大腸直腸癌適應症。
- 在報告與決策中明確標註：療效僅歸因於 S-1 複方，不可外推到 oteracil 單方。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

