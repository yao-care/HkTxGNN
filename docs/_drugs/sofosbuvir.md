---
layout: default
title: Sofosbuvir
parent: 僅模型預測 (L5)
nav_order: 810
evidence_level: L5
indication_count: 5
---

# Sofosbuvir
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

# Sofosbuvir：從 C 型肝炎到 B 型肝炎病毒感染

## 一句話總結

Sofosbuvir 是 C 型肝炎 (HCV) 直接作用抗病毒藥物，在香港以 Epclusa、Vosevi 兩種複方上市。
TxGNN 模型預測它可能對 **B 型肝炎病毒感染 (Hepatitis B virus infection)** 有效。
目前有 1 個直接針對 HBV 的 Phase 2 單臂試驗（21 人）可參考，但沒有 RCT，且多數文獻顯示的是 HBV 再活化風險，而非療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | B 型肝炎病毒感染 (Hepatitis B virus infection) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L4（證據包評定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Sofosbuvir 是核苷酸類似物，抑制 HCV 的 NS5B RNA 聚合酶。HBV 則是靠反轉錄酶／DNA 聚合酶複製，所以機轉上沒有明確的直接抗病毒連結。

TxGNN 的高分（99.77%）較可能反映知識圖譜中它與 HCV、肝炎的網絡鄰近性，而不是已知的抗 HBV 活性。

臨床上確實有一個訊號：Phase 2 單臂研究（PMID 36045503）觀察到，HBV 單一感染者使用 ledipasvir/sofosbuvir 後 HBsAg 有小幅下降。這來自 HBV/HCV 共感染者的回溯觀察，但樣本小、無對照組，不足以證明療效。另一方面，多項研究報告 HCV 清除後出現 HBV 再活化，安全性訊號與預測方向相反。

## 臨床試驗證據

證據包列出的 50 個試驗中，絕大多數是 HCV 療效或給藥模式研究，與 HBV 療效無關。下表僅列與 HBV 直接相關者：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | 完成 | 21 | Ledipasvir/sofosbuvir 12 週用於 HBV 感染者，評估 HBsAg 與 HBV DNA 變化 |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 完成 | 23 | HCV/HBV 共感染者接受抗 HCV 藥物期間，HBV 再活化的發生率與危險因子 |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | 完成 | 111 | 台灣 HCV/HBV 共感染者使用 ledipasvir/sofosbuvir 的抗病毒療效與安全性（主要終點為 HCV） |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | 未知 | 120 | 中國 HCV/HBV 共感染者使用 SOF/VEL 並預防性併用 TAF，監測 HBV 再活化 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 單臂試驗 | J Med Virol | HBV 單一感染者使用 LDV/SOF 12 週，以 HBsAg 下降為主要終點，訊號有限 |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | 追蹤研究 | Clin Infect Dis | 台灣 HCV/HBV 共感染者使用 LDV/SOF 後追蹤 108 週，評估 HBV 再活化 |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | 世代研究 | Trans R Soc Trop Med Hyg | 埃及 HCV 與 HCV/HBV 共感染者使用 sofosbuvir/daclatasvir 的療效 |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | 研究 | J Clin Gastroenterol | 評估 ledipasvir-sofosbuvir 治療期間 HBV 再活化的風險 |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | 前瞻觀察研究 | J Viral Hepat | 癌症病人接受抗 HCV 藥物期間的 HBV 再活化 |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | 病例報告＋文獻回顧 | Medicine | Sofosbuvir＋ribavirin 治癒 HCV 後發生 HBV 再活化 |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | 流行病學模型 | Lancet Gastroenterol Hepatol | 2022 年全球 HBV 盛行率與照護cascade（背景資料） |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65046 | EPCLUSA TABLETS 400MG/100MG | GILEAD SCIENCES HONG KONG LIMITED |
| HK-65775 | VOSEVI TABLETS | GILEAD SCIENCES HONG KONG LIMITED |

## 安全性考量

證據包中沒有仿單警語、禁忌症與藥物交互作用資料，請參考原廠仿單。

- **HBV 再活化（文獻訊號）**：多篇研究顯示，HBV 感染者或曾暴露者在使用含 sofosbuvir 的 HCV 治療期間或之後，可能發生 HBV 再活化（如 PMID 33031326、29334502、33523503）。這與「用於治療 HBV」的方向直接衝突。

## 結論與下一步

**決策：Hold**

**理由：**
- Sofosbuvir 與 HBV 複製機轉沒有直接連結，TxGNN 高分較可能來自網絡鄰近性。
- 唯一直接相關的是小型單臂 Phase 2 研究，證據不足以支持療效。
- 文獻中的 HBV 再活化訊號，使安全性顧慮高於潛在效益。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，並完成 S1 安全性篩選。
- 補充 DrugBank 的作用機轉資料。
- 取得 NCT03312023 的完整結果，評估 HBsAg 下降幅度是否具臨床意義。
- 若仍要探索，需有 HBV 單一感染者的對照試驗，並納入再活化監測計畫。
- 同一藥物的預測中，**E 型肝炎病毒感染**（排名第 2，體外與小型病例報告有證據，證據等級 L3）機轉合理性較高，可優先評估。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

