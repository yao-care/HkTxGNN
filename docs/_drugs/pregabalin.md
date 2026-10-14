---
layout: default
title: Pregabalin
parent: 僅模型預測 (L5)
nav_order: 729
evidence_level: L5
indication_count: 5
---

# Pregabalin
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

# Pregabalin：從焦慮症、纖維肌痛到肌腱炎

predicted_indications[0] 為肌腱炎（tendinitis），但 rank 5 的偏頭痛（migraine disorder）證據明顯較充分。下文以 rank 1 為主軸，並在結論補充偏頭痛的比較。

## 一句話總結

Pregabalin 原本用於焦慮症、纖維肌痛、肌筋膜疼痛症候群與帶狀疱疹後神經痛。
TxGNN 模型預測它可能對**肌腱炎 (Tendinitis)** 有效，但目前**沒有相關臨床試驗**，且檢索到的 6 篇文獻皆未直接研究以 pregabalin 治療肌腱炎，證據僅停留在模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 焦慮症、纖維肌痛、肌筋膜疼痛症候群、帶狀疱疹後神經痛（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 肌腱炎 (Tendinitis) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L5（僅有模型預測，無直接研究；文獻評分標示為 L4，但內容未直接涉及肌腱炎） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠 MOA 欄位無資料）。依一般藥理知識，pregabalin 結合電壓閘控鈣離子通道的 α2δ 亞單位，減少興奮性神經傳導物質釋放，因此可緩解神經病變性或中樞敏感化的疼痛。

肌腱炎主要是發炎或退化性的肌肉骨骼疾病，與 pregabalin 已核准的神經痛、纖維肌痛、肌筋膜疼痛有部分疼痛機轉重疊，但關聯是間接的，最多只能作為疼痛控制的輔助。0.997 的高分是圖譜運算結果，不等於臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | 關節鏡肩袖修補術後，口服 pregabalin 的疼痛分數與肌間溝臂叢神經阻斷相當；屬術後鎮痛，非肌腱炎治療 |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | 回溯性世代研究 | J Orthop Sci | 評估肩袖修補術後 pregabalin 的鎮痛與減少鴉片類用量效果；非肌腱炎 |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | 病例報告/回顧 | Praxis | 環丙沙星相關氟喹諾酮失能（含肌腱病變等副作用）；與 pregabalin 治療無關 |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | 病例報告 | Pain Pract | 馬拉松後股後皮神經壓迫，與腿後肌腱炎相關；未評估 pregabalin |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | 社論 | Arthroscopy | 梨狀肌症候群的診斷與坐骨神經鬆解；與 pregabalin 無關 |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | 前臨床（動物） | Adv Pharmacol Pharm Sci | 植物萃取物改善長春新鹼誘發的大鼠神經病變；與 pregabalin 治療肌腱炎無關 |

## 香港上市資訊

下表列出 5 張主要許可證（共 20 張，皆為有效單方製劑；資料中未載明劑型與核准適應症文字）。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53029 | LYRICA CAP 25MG | 膠囊 | 未載明 |
| HK-53026 | LYRICA CAP 300MG | 膠囊 | 未載明 |
| HK-62124 | BRILLIOR CAPSULES 50MG | 膠囊 | 未載明 |
| HK-63581 | PREGABALIN SANDOZ CAPSULES 50MG | 膠囊 | 未載明 |
| HK-68026 | PREGABALIN TEVA CAPSULES 25MG | 膠囊 | 未載明 |

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（非仿單內容）：焦慮症、神經症、輕鬱症、血小板低下、血管性水腫（含遺傳性與後天性）、肌病變與肌肉疾病、橫紋肌溶解症、家族性週期性麻痺、結節性筋膜炎、腎功能不全、房室傳導阻滯。
- **藥物交互作用**：共查得 100 筆，以下為主要項目。
  - 重大（Major）：Morphine、Morphine（脂質體）。
  - 中度（Moderate）：Pioglitazone、Rosiglitazone、Troglitazone、Difenoxin、Diphenoxylate、Dronabinol、Nabilone、Metoclopramide、Opium、Sibutramine。
- 與鴉片類併用的中樞神經與呼吸抑制風險需特別留意。
- 完整警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 肌腱炎沒有任何臨床試驗，文獻也都不是直接研究 pregabalin 治療肌腱炎，僅有 0.997 的模型分數。
- 作用機轉的連結間接，最多是疼痛輔助，無法改善肌腱病變本身。

**若要推進需要：**
- 設計 pregabalin 用於肌腱炎（或肌腱病變）疼痛的對照試驗。
- 取得詳細的作用機轉資料，並取得香港仿單的警語與禁忌。
- 評估肌病變、腎功能不全等圖譜標示風險在目標族群的影響。

**補充：其他預測適應症比較**
- **偏頭痛（rank 5，分數 99.47%）**：有 1 個 Phase 3 試驗（NCT00447369），但已撤回、無數據；另有數項兒童隨機試驗（pregabalin 對比 valproate、propranolol）與網絡統合分析，證據評為 L2，屬值得進一步研究的方向，但多為小型兒科研究，需要確認性試驗。
- **肌纖維化（myositis fibrosa）、特發性肉芽腫性肌炎、包涵體肌炎**：無相關研究，僅有模型預測，皆建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

