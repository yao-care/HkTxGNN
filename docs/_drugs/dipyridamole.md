---
layout: default
title: Dipyridamole
parent: 中證據等級 (L3-L4)
nav_order: 280
evidence_level: L4
indication_count: 10
---

# Dipyridamole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Dipyridamole：從（原適應症資料未載）到變異型心絞痛

## 一句話總結

Dipyridamole（雙嘧達莫）在香港已有 10 張上市許可證，但證據包中沒有記載原適應症。
TxGNN 模型預測它可能對**變異型心絞痛 (Prinzmetal angina)** 有效，
目前**沒有臨床試驗**，只有 **15 篇文獻**，且多數是把它當診斷用的壓力／誘發試驗藥物，並非治療證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 變異型心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Dipyridamole 會抑制腺苷再攝取，使腺苷濃度上升，進而造成冠狀動脈擴張。從這個角度看，它與心絞痛在機轉上有關聯，這可能是模型給出高分的原因。

但文獻多把它當作診斷用的壓力或誘發藥物，而不是治療藥物。例如有研究描述，在變異型心絞痛病人身上，Dipyridamole 壓力試驗結束時（以 aminophylline 快速逆轉血管擴張）可能誘發冠狀動脈痙攣。冠狀動脈竊血 (coronary steal) 與痙攣誘發也是合理的安全疑慮。

因此目前的證據**不支持治療效益**，模型的高分較可能反映知識圖譜上的關聯，並非療效訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

現有文獻中沒有 RCT，以下依相關性列出 10 篇：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | 臨床研究 | Jpn Circ J | 26 位休息型心絞痛病人（含 13 位變異型）試用多種藥物，包括 Dipyridamole 50 mg。Propranolol 無法抑制發作，反而傾向加重；摘要片段未呈現 Dipyridamole 的結果 |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | 小型臨床系列 | Am J Cardiol | 36 位住院病人。Dipyridamole 壓力試驗後以 aminophylline 終止，可能透過血管痙攣機轉誘發變異型心絞痛缺血 |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | 世代研究 | Br Heart J | 25 位運動誘發 ST 段上升的病人，依 Dipyridamole 試驗反應分組，評估運動試驗的短期再現性 |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | 世代研究 | Zhonghua Xin Xue Guan Bing Za Zhi | 比較典型與非典型冠狀動脈痙攣的臨床特徵；摘要未提供 Dipyridamole 相關細節 |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | 回顧 | Jpn Circ J | Dipyridamole 負荷鉈-201 心肌造影診斷冠心病準確度 66%；合併運動負荷後敏感度由 71% 升至 87% |
| [8417062](https://pubmed.ncbi.nlm.nih.gov/8417062/) | 1993 | 臨床研究 | J Am Coll Cardiol | 探討不同機轉誘發的缺血中，暫時性無收縮心肌的回音密度增加，作為缺血的新超音波徵象 |
| [8634169](https://pubmed.ncbi.nlm.nih.gov/8634169/) | 1996 | 世代研究 | Rev Port Cardiol | 疑似冠心病且 Dipyridamole-鉈心肌掃描正常者的 3 年預後追蹤 |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | 回顧 | Circulation | 從病理生理角度討論冠狀動脈狹窄的非侵入性功能評估（含 Dipyridamole 等刺激方法） |
| [7628141](https://pubmed.ncbi.nlm.nih.gov/7628141/) | 1995 | 病例報告 | Clin Nucl Med | 一位有偏頭痛、氣喘與變異型心絞痛病史的病人，掃描顯示下壁與後壁缺血，討論「心臟型偏頭痛」是否為獨立臨床實體 |
| [2221701](https://pubmed.ncbi.nlm.nih.gov/2221701/) | 1990 | 回顧 | Ann N Y Acad Sci | 暫時性心肌缺血的心電圖診斷敏感度與特異度（無摘要） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-15915 | DIPYRIDAMOLE S C TAB 25MG | 未載明 | 未載明 |
| HK-35124 | PROCARDIN 75 TAB 75MG | 未載明 | 未載明 |
| HK-39893 | APO-DIPYRIDAMOLE FC TAB 25MG | 未載明 | 未載明 |
| HK-67900 | WYSIN TABLETS 25MG | 未載明 | 未載明 |
| HK-55039 | LIDAMOLE F.C. TAB "S.C." 25MG | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

文獻提示的風險：Dipyridamole 可能造成冠狀動脈竊血，並有文獻指出可能誘發血管痙攣。用於變異型心絞痛病人時，這兩點需要特別留意。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻也多為診斷用途，且有誘發痙攣的安全疑慮，不支持治療效益。
- 預測分數雖高，但證據等級僅 L4。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，並補齊原適應症與各許可證的核准適應症（目前皆為空白）。
- 補充 Dipyridamole 的作用機轉資料（例如查詢 DrugBank）。
- 收集 Dipyridamole 用於變異型心絞痛的治療性研究，並評估冠狀動脈竊血與痙攣的風險。
- 排名第 2 的中風與第 5 的短暫性腦缺血發作 (TIA) 雖有 L1 等級證據，但 Dipyridamole 合併 aspirin 用於次級預防早已是核准且列入指引的用途，很可能不算真正的老藥新用。若要作為新候選，須先對照仿單核實。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

