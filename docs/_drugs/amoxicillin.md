---
layout: default
title: Amoxicillin
parent: 僅模型預測 (L5)
nav_order: 49
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Amoxicillin：從細菌感染到多株型高黏滯度症候群

## 一句話總結

Amoxicillin 是廣效性 β-內醯胺類抗生素，廣泛用於多種細菌性感染治療。
TxGNN 模型的頂排預測指向**多株型高黏滯度症候群 (Polyclonal Hyperviscosity Syndrome)**，然而此預測**零臨床試驗、零文獻支持（L5）**，極可能為知識圖譜拓撲偽關聯。
在全部 8 個預測中，**單株免疫球蛋白病變（Rank 6）** 具備病原驅動的機轉合理性，是值得進一步關注的研究方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣效性細菌感染（香港無上市許可資料） |
| 預測新適應症 | 多株型高黏滯度症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

### Amoxicillin 的作用機轉

本 Evidence Pack 標記 MOA 為資料缺口，但 Amoxicillin 的作用機轉已充分建立於藥理文獻中。作為廣效性 β-內醯胺類抗生素，它透過不可逆結合細菌細胞壁合成所需的**青黴素結合蛋白（PBPs）**，抑制肽聚醣（peptidoglycan）交聯反應，導致細菌細胞壁完整性崩潰、溶菌死亡。此機轉**專一作用於細菌**，對宿主細胞無直接藥理效應。

### 頂排預測的合理性評估（Rank 1）

**多株型高黏滯度症候群** 通常由多株免疫球蛋白異常升高引起，見於慢性感染、自體免疫疾病等情境，核心病理為蛋白質介導的血液流變異常，與 Amoxicillin 的細菌細胞壁抑制機轉**無直接病理連結**。TxGNN 高分（99.63%）極可能源自知識圖譜中血液/免疫疾病節點的系統性過度連結，屬**模型拓撲偽關聯**，不構成再利用依據。

此外，Rank 2（hyperamylasemia）與 Rank 1 的 TxGNN 分數完全相同（0.9963032007217408），強烈提示批次計算偽影。Rank 3（先天性無白蛋白血症）為遺傳性蛋白合成缺陷，亦無機轉連結可言。

### 具機轉合理性的預測

在 8 個預測中，以下兩者具備相對合理的機轉連結：

**Rank 6 — 單株免疫球蛋白病變（Monoclonal Gammopathy）**：特定子類型「免疫增殖性小腸疾病（IPSID）/地中海淋巴瘤/α 重鏈病」的發病與 *Campylobacter jejuni* 慢性感染驅動相關。抗生素根除感染可去除抗原刺激，導致單株 B 細胞增殖逆轉——即「病原驅動→抗菌清除→腫瘤退縮」的間接再利用邏輯。Amoxicillin 為此類 IPSID 抗菌治療方案的核心藥物，有案例系列和歷史隊列支持（L4）。注意此機轉**不適用於 MGUS 或多發性骨髓瘤**等非感染驅動型單株免疫球蛋白病變。

**Rank 8 — 敗血性鼠疫（Septicemic Plague）**：Amoxicillin 對 *Yersinia pestis* 具體外抑菌活性，動物模型亦顯示療效。然而現行 WHO/CDC 指引優先選用鏈黴素、慶大黴素或多西環素，且存在 β-內醯胺酶耐藥性（blaA/blaB 基因）顧慮，缺乏人體 RCT（L4）。

---

## 臨床試驗證據

目前無 Amoxicillin 用於**多株型高黏滯度症候群**的相關臨床試驗登記。

### 補充：單株免疫球蛋白病變（Rank 6）相關試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | NA | 已終止 | 351 | 比較 Moxifloxacin 單藥 vs. Ciprofloxacin + Amoxicillin 用於嗜中性球低下腫瘤患者發燒的經驗性口服抗菌治療。研究對象為廣泛腫瘤患者，非單株免疫球蛋白病變治療研究，相關性低（C 級）。 |

---

## 文獻證據

目前無 Amoxicillin 用於**多株型高黏滯度症候群**的相關文獻。

### 補充：單株免疫球蛋白病變（Rank 6）—— 具機轉關聯文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9030995](https://pubmed.ncbi.nlm.nih.gov/9030995/) | 1996 | Case Series / Historical Cohort | Internal Medicine (Tokyo) | 74 歲女性地中海淋巴瘤（α 重鏈病）以抗生素治療後緩解，提供抗菌治療可逆轉 IPSID 的早期案例依據 |
| [20300878](https://pubmed.ncbi.nlm.nih.gov/20300878/) | 2010 | Case Series | J Gastrointestinal Cancer | 免疫增殖性小腸疾病合併 *H. pylori* 感染，根除治療後疾病退縮 |
| [8988128](https://pubmed.ncbi.nlm.nih.gov/8988128/) | 1997 | Case Report | Lancet | 免疫增殖性小腸疾病根除 *H. pylori* 後緩解之早期 Lancet 報告 |
| [21908119](https://pubmed.ncbi.nlm.nih.gov/21908119/) | 2011 | Case Report | Méd Mal Infect | Rothia dentocariosa 肺炎合併血液惡性疾病情境，Amoxicillin 為治療用藥 |
| [35619805](https://pubmed.ncbi.nlm.nih.gov/35619805/) | 2022 | Case Report | Front Public Health | 巨球蛋白血症患者播散性 *Nocardia vulneris* 感染，Amoxicillin/clavulanic 為藥敏選項之一 |

### 補充：敗血性鼠疫（Rank 8）相關文獻

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal Model Study | Antimicrob Agents Chemother | Amoxicillin 在鼠疫菌系統感染小鼠模型中顯示體外及體內抑菌活性，與鏈黴素等標準藥物比較 |
| [21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/) | 2011 | In Vitro Study | Antimicrob Agents Chemother | 評估多種抗生素對胞內 *Y. pestis* 的殺菌效力，為機轉層面的體外依據 |
| [3957763](https://pubmed.ncbi.nlm.nih.gov/3957763/) | 1986 | Case Report (Veterinary) | JAVMA | 貓腺鼠疫以 Amoxicillin + Streptomycin 成功治療，屬非人體情境使用 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（頂排預測 — 多株型高黏滯度症候群）**

**理由：**
Amoxicillin 對多株型高黏滯度症候群的 TxGNN 高分預測缺乏機轉合理性，且無任何臨床試驗或文獻支持；相同分數出現在多個預測中（批次計算偽影），進一步確認此預測為知識圖譜系統性偽關聯，不建議推進。

---

### 附：全部 8 個預測決策摘要

| 排名 | 適應症 | 證據等級 | 建議 | 備註 |
|------|--------|---------|------|------|
| 1 | 多株型高黏滯度症候群 | L5 | Hold | 無機轉連結，模型偽關聯 |
| 2 | 高澱粉酶血症 | L5 | Hold | TxGNN 分數與 Rank 1 完全相同，批次計算偽影 |
| 3 | 先天性無白蛋白血症 | L5 | Hold | 遺傳性合成缺陷，Amoxicillin 無任何病理連結 |
| 4 | 血型不相容 | L5 | Hold | 唯一文獻（PMID 40350274）為感染情境性使用，非再利用依據 |
| 5 | 血液系統前惡性疾病 | L5 | Hold | 克隆演化病理，無抗菌機轉連結 |
| **6** | **單株免疫球蛋白病變** | **L4** | **Research Question** | **IPSID 子類型具病原驅動機轉，有案例系列支持** |
| 7 | 血液病合併後天性周邊神經病變 | L5 | Hold | 免疫/副腫瘤機轉，無機轉連結 |
| **8** | **敗血性鼠疫** | **L4** | **Research Question** | **體外/動物實驗有依據，缺乏人體 RCT，耐藥性顧慮** |

---

**若要推進（Rank 6：單株免疫球蛋白病變 / IPSID）需要：**
- 取得香港 (Department of Health) Amoxicillin 上市許可及核准適應症資料
- 補充 Amoxicillin 完整 MOA 及安全性資訊（TFDA 仿單 PDF 解析或 DrugBank API）
- 系統性回顧 IPSID 標準治療指引中 Amoxicillin（含/不含 metronidazole）的使用證據
- 評估是否有機會設計聚焦 IPSID 族群的小型前瞻性佇列研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

