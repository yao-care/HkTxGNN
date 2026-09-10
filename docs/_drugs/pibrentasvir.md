---
layout: default
title: Pibrentasvir
parent: 中證據等級 (L3-L4)
nav_order: 584
evidence_level: L4
indication_count: 5
---

# Pibrentasvir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Pibrentasvir：從 C型肝炎（複方成分）到 B型肝炎病毒感染

## 一句話總結

Pibrentasvir 是 Glecaprevir/Pibrentasvir（Mavyret）複方中的 NS5A 抑制劑成分，目前所有臨床證據皆圍繞 **C型肝炎（HCV）** 治療。TxGNN 模型預測它可能對 **B型肝炎病毒感染 (Hepatitis B virus infection)** 有效，雖有 14 個臨床試驗與 20 篇文獻可查，但**逐一檢視後皆為 HCV 治療研究（部分收案含 HBV 共感染者作為背景），並無直接支持 HBV 療效的證據**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | C型肝炎（Glecaprevir/Pibrentasvir 複方成分；正式 MOA／適應症資料缺失） |
| 預測新適應症 | B型肝炎病毒感染 (Hepatitis B virus infection) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

**這個預測目前缺乏機轉支持，證據審查後判定不合理。**

Pibrentasvir 專一抑制 HCV NS5A 蛋白，其標靶是 HCV RNA 複製複合體。HBV 則是具反轉錄酶的 DNA 病毒，複製機制與 HCV 完全不同，HBV 生命週期中沒有與 NS5A 同源的標靶蛋白，藥理上沒有交叉作用的基礎。

所列出的 14 個臨床試驗與 20 篇文獻經逐一檢視，全部是 Glecaprevir/Pibrentasvir 治療慢性 C型肝炎 的臨床計畫；部分收案族群含 HBV/HCV 共感染者，但治療目標與主要結局皆是清除 HCV（如 SVR12），HBV 僅為背景共病或監測項目，並非藥物介入對象。TxGNN 給出的高分，較可能反映知識圖譜中「病毒性肝炎」語意群聚造成的假陽性關聯，而非真實的機轉關聯性。

*（同一份 Evidence Pack 中，其餘四個候選適應症——HIV、E型肝炎、A型肝炎、動物病毒性肝炎——同樣呈現此模式：證據審查結論均為機轉不支持或無直接佐證，評分等級為 L4-L5，建議皆為 Hold。這顯示本次 TxGNN 批次預測對 Pibrentasvir 整體呈現系統性假陽性訊號。）*

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Phase 2 | 完成 | 89 | ABT-493/ABT-530 多劑量安全性與抗病毒活性，genotype 1 HCV |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Phase 3 | 完成 | 506 | ENDURANCE-3：GLE/PIB vs Sofosbuvir+Daclatasvir，genotype 3 HCV |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | 完成 | 87 | HIV/HCV 治癒後心血管風險追蹤，非藥物介入 HBV 試驗 |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Phase 3 | 完成 | 295 | CERTAIN-1：日本成人 HCV 療效安全性 |
| [NCT02723084](https://clinicaltrials.gov/study/NCT02723084) | Phase 3 | 完成 | 136 | CERTAIN-2：日本 genotype 2 HCV 療效安全性 |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Phase 3 | 完成 | 100 | 巴西 genotype 1-6 HCV 未治療族群療效安全性 |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Phase 2/3 | 完成 | 141 | 前次 DAA 治療失敗之 HCV 再治療 |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Phase 2/3 | 完成 | 384 | HCV 患者長期追蹤：抗藥性持續性與 SVR 耐久性 |
| [NCT02243293](https://clinicaltrials.gov/study/NCT02243293) | Phase 2/3 | 完成 | 694 | SURVEYOR-II：genotype 2/3/4/5/6 HCV 療效安全性 |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Phase 3 | 完成 | 304 | ENDURANCE-2：genotype 2 HCV 療效安全性（雙盲安慰劑對照） |

**所有列出試驗的治療目標皆為 HCV，無任一試驗以 HBV 感染作為主要適應症或療效指標。**

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34344581](https://pubmed.ncbi.nlm.nih.gov/34344581/) | 2021 | Case Report | J Infect Chemother | 化療誘發 HCV 急性惡化案例報告；提及 HBV 再活化為更常見情境，但本案主角為 HCV |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | pending | Klin Mikrobiol Infekc Lek | 兒童慢性病毒性肝炎 B 與 C 之抗病毒治療回溯性評估 |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | pending | Annals of Hepatology | 全球 HBV 與 HCV 抗病毒藥物定價比較 |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | pending | World J Gastroenterol | 兒童病毒性肝炎（HBV/HCV）治療進展回顧，HBV 治療仍非治癒性 |
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Review | Lancet Infect Dis | 討論 HCV 治療後之 HBV 疫苗接種議題，非 Pibrentasvir 對 HBV 療效 |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepat | GLE/PIB 於嚴重腎功能不全 HCV 患者的真實世界療效安全性（台灣） |
| [35431505](https://pubmed.ncbi.nlm.nih.gov/35431505/) | 2022 | Cohort | World J Gastroenterol | HIV/HCV genotype 6 共感染者 DAA 真實世界療效 |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | pending | Eur J Gen Pract | 慢性 C型肝炎診斷與治療綜覽 |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | pending | Lancet Gastroenterol Hepatol | 兒童與青少年 HCV 感染治療現況 |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | pending | Semin Liver Dis | DAA 治療失敗 HCV 患者之再治療策略 |

**無任一文獻報告 Pibrentasvir 對 HBV 之直接抗病毒療效或臨床試驗結果。**

## 香港上市資訊

此藥物目前**未在香港上市**，查無許可證登記資料。

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：Evidence Pack 標記 TFDA/香港仿單警語與禁忌症資料缺失（DG001，Blocking 等級），此為進入 S1 安全性初評的阻斷性缺口，需優先補齊。

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉層面 NS5A 抑制劑與 HBV 複製機制無同源標靶，證據審查確認現有 14 個臨床試驗、20 篇文獻皆為 HCV 治療研究，未提供 HBV 療效之直接支持；TxGNN 高分推測為知識圖譜「病毒性肝炎」語意群聚導致的假陽性訊號。
- 仿單警語／禁忌症資料缺失屬 Blocking 等級（DG001），無法進行安全性初評，本身已構成推進障礙。

**若要推進需要：**
- 補齊 MOA 正式資料與仿單警語／禁忌症（解除 DG001、DG002）
- 若仍欲探索 HBV 適應症，需先取得體外／動物模式的直接抗 HBV 藥效學證據，證明 NS5A 抑制劑對 HBV 複製有實質抑制作用
- 重新檢視 TxGNN 對本藥物的其餘預測結果（HIV、HEV、HAV 等候選皆呈現相同假陽性模式），評估是否為該藥物節點在知識圖譜中的嵌入異常
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

