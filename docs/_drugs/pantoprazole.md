---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 650
evidence_level: L5
indication_count: 5
---

# Pantoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Pantoprazole：從胃酸相關疾病到活動性消化性潰瘍

## 一句話總結

Pantoprazole 是質子幫浦抑制劑（PPI），透過抑制胃酸分泌來治療胃酸相關疾病。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
目前有 **3 個臨床試驗**和 **20 篇文獻**支持這個方向。
消化性潰瘍本身是 pantoprazole 的核心適應症，因此這項預測更接近「既有用途的驗證」，而非真正的新用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L2（僅 1 個已完成的 Phase 3 RCT，且該試驗中 pantoprazole 可能是對照藥；Evidence Pack 預評為 L1） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Pantoprazole 不可逆地抑制胃壁細胞的 H+/K+ ATPase（質子幫浦），阻斷胃酸分泌的最後一步。
胃酸下降後，潰瘍得以癒合。胃內 pH 值升高，也有助於出血性潰瘍的血栓穩定，並提升合併抗生素時的幽門螺旋桿菌 (H. pylori) 根除率。

DrugBank 的作用機轉欄位目前缺漏，上述機轉說明來自 Evidence Pack 的推論與文獻摘要。
香港許可證的適應症文字也是空白，無法從登記資料確認原適應症。
但文獻一致將 PPI 列為消化性潰瘍、H. pylori 感染與胃食道逆流的首選用藥。

因此，TxGNN 給出高分（排名第 6357）符合藥理預期。
重點在於驗證：pantoprazole 本身（而非同類藥）在潰瘍癒合、出血後再出血預防、H. pylori 根除三合療法中的直接證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | 完成 | 323 | 隨機、雙盲、活性對照；比較 Ilaprazole 與 Pantoprazole 7 天三合療法，用於 H. pylori 陽性的胃／十二指腸潰瘍。尚未公布結果，且 pantoprazole 可能是對照藥 |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | 完成 | 316 | 找出出血性潰瘍止血後需二次內視鏡的風險因子，屬處置策略研究，非 pantoprazole 療效試驗 |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | 完成 | 320 | 評估 statin 與 PPI 對 clopidogrel 抗血小板作用的影響，屬藥物交互作用議題，非潰瘍治療 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | 比較間歇與持續輸注 pantoprazole 對潰瘍出血內視鏡治療後再出血的影響 |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT（依標題推斷） | J Gastroenterol Hepatol | 評估 pantoprazole 輸注作為內視鏡治療輔助，能否改善潰瘍出血結果 |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT（依標題推斷） | Aliment Pharmacol Ther | 比較三種 pantoprazole 三合療法的 H. pylori 根除與胃潰瘍癒合 |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | RCT（依標題推斷） | Aliment Pharmacol Ther | Pantoprazole、amoxicillin 搭配 azithromycin 或 clarithromycin，用於十二指腸潰瘍的 H. pylori 根除 |
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | 臨床研究（設計不明） | Hepato-gastroenterology | 比較 lansoprazole 與 pantoprazole 治療活動性十二指腸潰瘍及根除 H. pylori 的效果 |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 系統性回顧／網絡統合分析 | Am J Gastroenterol | 比較 P-CAB 與 PPI 治療 LA 分級 C/D 食道炎的療效與安全性（疾病為食道炎，間接相關） |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clin Drug Investig | Pantoprazole 專一性結合質子幫浦，作用時間較長；摘要指出多項研究未發現藥物交互作用 |
| [9017763](https://pubmed.ncbi.nlm.nih.gov/9017763/) | 1997 | Review | Pharmacotherapy | PPI（含 pantoprazole）控制胃酸的效果優於 H2 受體拮抗劑 |
| [10983736](https://pubmed.ncbi.nlm.nih.gov/10983736/) | 2000 | Review | Drugs | Esomeprazole 的綜述，內容含與 pantoprazole 的胃內 pH 控制比較 |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | 前臨床（動物模型） | Inflammopharmacology | 大鼠胃潰瘍模型中，pantoprazole 合併間質幹細胞對潰瘍癒合的影響 |

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。登記資料中的劑型與核准適應症欄位為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60028 | PANTOPRAZOLE POWDER FOR SOLUTION FOR INJ 40MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-68004 | REPRAT GASTRO-RESISTANT TABLETS 20MG | MEDILINE (HONG KONG) COMPANY LIMITED |
| HK-63999 | TECTA GASTRO-RESISTANT TABLETS 40MG | TAKEDA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-63772 | ALPANZOLE POWDER FOR SOLUTION FOR INJECTION 40MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-59424 | PANTOPRAZOLE SANDOZ TAB 20MG | SANDOZ HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 潰瘍出血、H. pylori 根除三合療法與潰瘍癒合方面，有多篇 pantoprazole 相關 RCT 與綜述支持，機轉明確，且香港已有 20 張許可證。
- 但已完成的 Phase 3 試驗只有 1 個，且 pantoprazole 可能是對照藥。香港仿單的警語與禁忌資料也缺漏（Evidence Pack 標示為阻擋性缺口），所以需加上防護條件。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌症與適應症文字，完成安全性篩選。
- 確認 NCT02084420 的實際分組，確認 pantoprazole 的角色（試驗藥或對照藥）。
- 取得 DrugBank 的作用機轉與藥物交互作用資料。
- 逐篇確認標示為「依標題推斷」的 RCT 之研究設計與結果。
- 評估與 clopidogrel 等併用藥物的交互作用風險（可參考 NCT00930670 的結果）。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

