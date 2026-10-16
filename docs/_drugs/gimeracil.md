---
layout: default
title: Gimeracil
parent: 高證據等級 (L1-L2)
nav_order: 414
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Gimeracil：預測新適應症為大腸腫瘤 (Colonic Neoplasm)（證據等級 L1）。原適應症：胃癌"
monitor_inn: "GIMERACIL"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "malignant gastric granular cell tumor", "lipoma of colon", "cecum neuroendocrine tumor G1"]
---

# Gimeracil
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Gimeracil：從胃癌到大腸腫瘤

## 一句話總結

Gimeracil 是 S-1 複方（tegafur／gimeracil／oteracil）的成分之一，原本用於胃癌治療。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效，
目前有 **6 個臨床試驗**和 **12 篇文獻**支持這個方向（所有證據均來自 S-1 複方，並非 gimeracil 單獨使用）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Gimeracil 是 S-1 中的 DPD（二氫嘧啶去氫酶）抑制劑。抑制 DPD 後，tegafur 轉換出的 5-FU 降解變慢，可維持較高且較持久的 5-FU 暴露量。

5-FU 是大腸直腸癌治療的核心抗代謝藥物，因此這個機轉與大腸腫瘤直接相關。胃癌與大腸腫瘤同屬消化道腫瘤，對氟尿嘧啶類藥物都有反應。

需要注意：gimeracil 不會單獨給藥，所有證據都來自 S-1 複方。此外，目前缺乏詳細的作用機轉資料庫記載，以上機轉說明來自已知藥理與模型的推論。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 已完成 | 1535 | UFT+Leucovorin 對比 TS-1（S-1），用於 Stage III 結腸癌輔助治療 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 未知 | 1191 | SOX 對比 XELOX，用於 Stage III 大腸直腸癌輔助化療 |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | 未知 | 40 | S-1 + Bevacizumab，用於前線治療失敗後的無法切除或復發大腸直腸癌 |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | 未知 | 82 | Raltitrexed + S-1，用於標準化療失敗的轉移性大腸直腸癌 |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | 尚未招募 | 52 | Fruquintinib + S-1，用於晚期轉移性大腸直腸癌第三線治療 |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | 已終止 | 20 | S-1 與 Capecitabine 併用 Oxaliplatin 對冠狀動脈血流的影響（心臟安全性終點，非療效試驗） |

## 文獻證據

本次文獻多為個案報告與臨床前研究，沒有 RCT。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | 個案報告／回顧 | J Oncol Pharm Pract | S-1 引起高三酸甘油脂血症；S-1 為大腸直腸癌有效藥物之一 |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | 藥動學研究 | Gan To Kagaku Ryoho | 以小鼠腹膜轉移模型評估 S-1 用於大腸癌腹膜轉移 |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | 臨床前（異種移植） | Oncol Rep | Irinotecan 併用 S-1 可克服大腸癌異種移植對 5-FU 的抗藥性 |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | 回顧性分析 | Gan To Kagaku Ryoho | 87 位接受 S-1/irinotecan 的病人中，3–4 級血液毒性發生率為 16.1% |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | 個案報告 | Anticancer Res | S-1 併用 CPT-11 使大腸癌肝轉移達完全緩解 |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | 個案報告 | Gan To Kagaku Ryoho | SOX 併 panitumumab 降階治療後，成功進行兩階段肝切除 |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | 個案報告 | Gan To Kagaku Ryoho | 橫結腸癌合併肝轉移與門靜脈腫瘤栓塞，經化療後有效 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | 個案報告 | Eur J Dermatol | TS-1 引起紅皮症、廣泛黏膜受累及手足症候群 |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | 個案報告 | Gan To Kagaku Ryoho | Oxaliplatin 引起急性周邊神經病變合併尿滯留（病人曾使用 S-1） |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | 個案報告 | Gan To Kagaku Ryoho | 大腸癌術後腹膜復發，以腹腔鏡手術反覆切除 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67976 | TEGO CAPSULES 20MG/5.8MG/19.6MG | 未載明 | 未載明 |
| HK-67977 | TEGO CAPSULES 25MG/7.25MG/24.5MG | 未載明 | 未載明 |
| HK-61181 | TS-ONE 25 CAP | 未載明 | 未載明 |
| HK-61182 | TS-ONE 20 CAP | 未載明 | 未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類複方；gimeracil 本身為 DPD 抑制劑，用以增強 5-FU） |
| 骨髓抑制風險 | 中度。文獻顯示 S-1 併用 irinotecan 時，3–4 級血液毒性發生率約 16.1% |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝腎功能、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

其他文獻記載的 S-1 相關不良反應包括手足症候群、紅皮症與黏膜病變、高三酸甘油脂血症。詳細警語請參考原廠仿單。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 1 個已完成的大型 Phase 3 試驗（NCT00660894，n=1535）直接評估 S-1 用於 Stage III 結腸癌，另有 1 個大型 Phase 3（NCT03448549，n=1191），機轉上與 5-FU 治療大腸癌的邏輯一致。
- 不過，所有證據均來自 S-1 複方而非 gimeracil 單藥；多數試驗狀態為「未知」，且文獻以個案報告和臨床前研究為主。仿單警語與禁忌資料也尚未取得，故需附帶條件推進。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症資料（目前為阻擋性資料缺口）
- 補充 DrugBank 的詳細作用機轉資料
- 取得 NCT00660894 與 NCT03448549 的最終結果，確認療效與安全性
- 確認 S-1 在香港的大腸直腸癌核准狀態，並建立 DPD 相關毒性與血液學監測計畫
- 其他排名較低的預測（如盲腸絨毛狀腺瘤、結腸脂肪瘤、盲腸神經內分泌腫瘤 G1 等）僅有模型預測、無臨床證據，且生物學上缺乏合理依據，不建議推進
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

